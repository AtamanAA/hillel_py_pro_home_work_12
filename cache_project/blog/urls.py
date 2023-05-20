from django.urls import path

from . import views


urlpatterns = [
    path("<int:publication_id>/", views.publication, name="publication"),
]
