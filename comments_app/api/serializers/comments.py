from rest_framework import serializers

from likes_app.services import is_fan
from tags_app.api.serializers.tag import TagSerializer
from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['user', ]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )
    tags = TagSerializer(many=True, read_only=True)

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return is_fan(obj, user)