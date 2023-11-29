from rest_framework import serializers
from .models import CustomUser
from django.utils.crypto import get_random_string


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "phone_number",
            "full_name",
            "password",
            "is_active",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            username=validated_data.get("username", ""),
            phone_number=validated_data.get("phone_number", ""),
            full_name=validated_data.get("full_name", ""),
            password=validated_data["password"],
            token_auth=get_random_string(64),
        )
        return user
