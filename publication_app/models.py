from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.PROTECT)
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=144, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    image = models.ImageField(null=True, blank=True)



