from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


class OTPVerifySerializer(serializers.Serializer):

    username = serializers.CharField()
    otp = serializers.CharField()