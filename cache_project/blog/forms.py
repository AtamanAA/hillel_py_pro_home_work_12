from django.forms import ModelForm
from blog.models import Publication


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ["title", "content"]
