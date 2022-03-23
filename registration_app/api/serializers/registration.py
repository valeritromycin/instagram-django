from rest_framework import serializers

from ...forms import RegistrationForm


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationForm
        exclude = ['password', ]
        extra_kwargs = {
            'file': {"required": True, 'read_only': True, "help_text": "New profile", }
        }

    password_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="password"
    )