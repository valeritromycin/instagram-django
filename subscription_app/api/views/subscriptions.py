from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.subscriptions import TagSubscriptionSerializer, UserSubscriptionSerializer
from ...models import Subscription


class SubscribeUserView(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = Subscription.objects.all()
    serializer_class = UserSubscriptionSerializer


class SubscribeTagView(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = Subscription.objects.all()
    serializer_class = TagSubscriptionSerializer


class SubscriptionsViewSet(GenericViewSet, ListModelMixin):
    queryset = Subscription.objects.all()
    serializer_class = UserSubscriptionSerializer
