from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, related_name="profile")
    phone_number = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(regex=r"^\+?\d{8,15}$", message="Неверный телефонный номер")],
        blank=True,
        null=True,
    )
    avatar = models.ImageField(blank=True, null=True),
    bio = models.TextField(blank=True, null=True),
    github = models.URLField(max_length=2048)