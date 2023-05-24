from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.cache import get_cache_key
from django.conf import settings

from .models import Publication
from .forms import PublicationForm


@cache_page(60 * 15)
def publication_read(request, publication_id):
    try:
        publication = Publication.objects.get(pk=publication_id)
    except Publication.DoesNotExist:
        message = f"<h1>Publication with ID: {publication_id} doesn't exist. Try another ID!</h1>"
        return HttpResponse(message)
    return render(request, "blog/publication.html", {"publication": publication})


def publication_update(request, publication_id):
    try:
        publication = Publication.objects.get(pk=publication_id)
    except Publication.DoesNotExist:
        message = f"<h1>Publication with ID: {publication_id} doesn't exist. Try another ID!</h1>"
        return HttpResponse(message)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=publication)
        if not form.is_valid():
            messages.error(request, "Form isn't valid. Try again!")
            return HttpResponseRedirect(
                reverse("publication_update", args=[form.instance.id])
            )
        form.save()

        expire_view_cache(request, publication_read, args=[publication_id])

        messages.success(
            request, f"Publication with ID {publication_id} update successful!"
        )
        return redirect("publication_read", publication_id=publication_id)
    else:
        form = PublicationForm(instance=publication)
        return render(request, "blog/publication_update.html", {"form": form})


def expire_view_cache(request, view_name, args=None, key_prefix=None):
    request_meta = {
        "SERVER_NAME": request.get_host().split(":")[0],
        "SERVER_PORT": request.get_host().split(":")[1],
    }

    request = HttpRequest()
    request.META = request_meta
    request.path = reverse(view_name, args=args)

    if settings.USE_I18N:
        request.LANGUAGE_CODE = settings.LANGUAGE_CODE

    cache_key = get_cache_key(request, key_prefix=key_prefix)
    if cache_key:
        if cache_key in cache:
            cache.delete(cache_key)
            return True
        else:
            return False
    else:
        raise ValueError("Failed to create cache_key")
