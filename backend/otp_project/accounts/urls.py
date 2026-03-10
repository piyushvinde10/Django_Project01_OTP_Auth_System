from django.urls import path
from .views import register_user, login_user, verify_otp

urlpatterns = [
    path("register/", register_user),
    path("login/", login_user),
    path("verify-otp/", verify_otp),
]