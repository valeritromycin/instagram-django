from django.db import models
from django.contrib.auth.models import User

from tags_app.models import Tag


class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name="+")
    subscription_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                          related_name="subscribers")
    subscription_tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True,
                                         related_name="subscribers")

    class Meta:
        unique_together = (('subscriber', 'subscription_user'),
                           ('subscriber', 'subscription_tag'))

