from rest_framework import routers

from registration_app.api.views.profile import ProfileViewSet

api_router = routers.DefaultRouter()

api_router.register('profile', ProfileViewSet)
