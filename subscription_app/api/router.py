from rest_framework import routers

from .views.subscriptions import SubscribeUserView, SubscribeTagView, SubscriptionsViewSet

api_router = routers.DefaultRouter()

api_router.register('subscribe/user', SubscribeUserView)
api_router.register('subscribe/tag', SubscribeTagView)
api_router.register('subscribe/all', SubscriptionsViewSet)

