from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from likes_app.api.serializers.likes import CommentLikeSerializer
from likes_app.models import Like
from tags_app.api.serializers.tag import TagSerializer
from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['user', ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )

    tags = TagSerializer(many=True, read_only=True)
    likes = CommentLikeSerializer(many=True, read_only=True)

    @extend_schema_field(bool)
    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        likes = Like.objects.filter(user=user, comment=obj.id)
        return likes.exists()

    @extend_schema_field(int)
    def get_likes_count(self, instance) -> int:
        return instance.likes.count()
