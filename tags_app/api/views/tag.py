from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.tag import TagSerializer, TagDetailSerializer
from ...models import Tag


class TagViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    actions_serializers = {'retrieve': TagDetailSerializer, }

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)
