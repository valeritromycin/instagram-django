from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.likes import PostLikeSerializer, CommentLikeSerializer
from ...models import Like


class LikePostView(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer


class LikeCommentView(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    queryset = Like.objects.all()
    serializer_class = CommentLikeSerializer
