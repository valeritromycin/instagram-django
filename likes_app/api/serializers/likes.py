from rest_framework import serializers
from ...models import Like


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ('user', 'comment')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ('user', 'post')

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )