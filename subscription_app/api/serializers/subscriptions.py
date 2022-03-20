from rest_framework import serializers
from ...models import Subscription


class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        read_only_fields = ['subscriber', ]
        exclude = ['subscription_tag']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="subscriber"
    )


class TagSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        read_only_fields = ['subscriber', ]
        exclude = ['subscription_user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="subscriber"
    )
