from django.db import models

from comments_app.models import Comment
from publication_app.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')
    comments = models.ManyToManyField(Comment, related_name='tags')
