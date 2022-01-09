from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator


class Post(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=144, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    image = models.ImageField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, related_name="profile")
    phone_number = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(regex=r"^\+?\d{8,15}$", message="Неверный телефонный номер")],
        blank=True,
        null=True,
    )
    bio = models.TextField(blank=True, null=True),
    github = models.URLField(max_length=2048)
