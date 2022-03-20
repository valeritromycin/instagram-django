from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from publication_app.api.serializers.publications import PostSerializer
from ..serializers.subscriptions import TagSubscriptionSerializer, UserSubscriptionSerializer
from ...models import Subscription


class SubscribeUserView(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = Subscription.objects.all()
    serializer_class = UserSubscriptionSerializer


class SubscribeTagView(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = Subscription.objects.all()
    serializer_class = TagSubscriptionSerializer


class SubscriptionsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Subscription.objects.all()
    serializer_class = UserSubscriptionSerializer

    @action(methods=["get", ], detail=False, name='subscription_users', serializer_class=UserSubscriptionSerializer)
    def user_posts(self, request, pk=None):
        instance = self.get_queryset().filter(subscription_user__isnull=False)
        return Response(self.get_serializer(instance, many=True).data)

    @action(methods=["get", ], detail=False, name='subscription_tags', serializer_class=TagSubscriptionSerializer)
    def tag_posts(self, request, pk=None):
        instance = self.get_queryset().filter(subscription_user__isnull=False)
        return Response(self.get_serializer(instance, many=True).data)