from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.profile import ProfileSerializer
from ...models import Profile


class ProfileViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [filters.OrderingFilter, ]
    ordering_fields = ['create_date', ]