from rest_framework import serializers

from ...models import Like


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ['user', 'comment']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )

    def validate(self, data):
        if self.context.get('request').user == data['post'].user.id:
            raise serializers.ValidationError("cannot like yourself")
        return data


class PostLikeDetailSerializer(PostLikeSerializer):
    class Meta:
        model = Like
        exclude = ['comment']


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ('user', 'post')

    def validate(self, data):
        if self.context.get('request').user == data['post'].user.id:
            raise serializers.ValidationError("cannot like yourself")
        return data

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )