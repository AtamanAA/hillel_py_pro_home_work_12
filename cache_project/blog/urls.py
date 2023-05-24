from django.urls import path

from . import views


urlpatterns = [
    path("<int:publication_id>/", views.publication_read, name="publication_read"),
    path(
        "<int:publication_id>/update/",
        views.publication_update,
        name="publication_update",
    ),
]
