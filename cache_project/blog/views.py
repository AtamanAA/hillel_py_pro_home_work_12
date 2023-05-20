from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import Publication
from .forms import PublicationForm


@cache_page(60 * 15)
def publication(request, publication_id):
    try:
        publication = Publication.objects.get(pk=publication_id)
    except Publication.DoesNotExist:
        message = f"<h1>Publication with ID: {publication_id} doesn't exist. Try another ID!</h1>"
        return HttpResponse(message)
    form = PublicationForm(instance=publication)
    return render(request, "blog/publication.html", {"form": form})
