from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.likes import PostLikeSerializer, CommentLikeSerializer
from ...models import Like


class LikePostView(GenericViewSet, CreateModelMixin):
    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer


class LikeCommentView(GenericViewSet, CreateModelMixin):
    queryset = Like.objects.all()
    serializer_class = CommentLikeSerializer
