from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, OTPVerifySerializer

User = get_user_model()


@api_view(["POST"])
def register_user(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_user(request):

    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)

        if user:

            otp = user.generate_otp()

            send_mail(
                "Your OTP Code",
                f"Your OTP is {otp}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return Response({"message": "OTP sent to email"})

        return Response({"error": "Invalid credentials"}, status=400)

    return Response(serializer.errors, status=400)


@api_view(["POST"])
def verify_otp(request):

    serializer = OTPVerifySerializer(data=request.data)

    if serializer.is_valid():

        username = serializer.validated_data["username"]
        otp = serializer.validated_data["otp"]

        try:
            user = User.objects.get(username=username)

            if user.verify_otp(otp):

                return Response({"message": "Login successful"})

            return Response({"error": "Invalid or expired OTP"}, status=400)

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

    return Response(serializer.errors, status=400)