from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Menu(models.Model):
    menu_label = models.CharField(max_length=256, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.id}: {self.menu_label}'


class MenuItem(models.Model):
    title = models.CharField(max_length=32, blank=False, null=False)
    url = models.CharField(max_length=256, blank=False, null=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=False, null=False, related_name='links')
    icon = models.ImageField(null=True, blank=True)
    priority = models.SmallIntegerField(validators=[MinValueValidator(-100), MaxValueValidator(100)], default=0)

    class Meta:
        indexes = [
            models.Index(fields=['url', 'menu']),
            models.Index(fields=['menu'])
        ]
        unique_together = [('menu', 'title'), ]

    def __str__(self):
        return f'{self.id}: {self.title}'
