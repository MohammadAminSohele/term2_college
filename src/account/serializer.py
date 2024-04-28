from django.utils.translation import gettext as _
from rest_framework import serializers 


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=20,
    )

    password = serializers.CharField(
        max_length=20,
    )


class UserRegisterSerializer(UserLoginSerializer):
    
    confirm_password = serializers.CharField(
        max_length=20,
    )

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError(
                {_("Error"): _("Your passwords didn't match.")}
            )

        return data
    
    first_name = serializers.CharField(
        max_length=50,
    )

    last_name = serializers.CharField(
        max_length=50,
    )

    email = serializers.CharField(
        max_length=200,
    )