from rest_framework import serializers

from tags_app.api.serializers.tag import TagSerializer
from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ['id', "user", ]
        exclude = ['is_public', ]
        extra_kwargs = {
            'file': {"required": True, 'write_only': True, "help_text": "ID Медиа Файла", }
        }

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )
    tags = TagSerializer(many=True, read_only=True)



