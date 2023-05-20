from django.db import models


class Publication(models.Model):
    DoesNotExist = None
    title = models.CharField(max_length=40)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
