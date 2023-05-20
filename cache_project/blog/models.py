from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    update_at = models.DateTimeField(auto_now=True)
