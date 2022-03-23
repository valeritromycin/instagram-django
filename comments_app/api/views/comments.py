from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.schemas import AutoSchema
from rest_framework.viewsets import GenericViewSet

from ..serializers.comments import CommentSerializer
from ...models import Comment


class CommentViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
