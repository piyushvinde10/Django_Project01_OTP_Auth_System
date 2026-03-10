from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import random


class User(AbstractUser):

    email = models.EmailField(unique=True)

    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)

    def generate_otp(self):
        otp_code = str(random.randint(100000, 999999))
        self.otp = otp_code
        self.otp_created_at = timezone.now()
        self.save()
        return otp_code

    def verify_otp(self, otp_code):

        if self.otp != otp_code:
            return False

        expiry_time = self.otp_created_at + timezone.timedelta(minutes=5)

        if timezone.now() > expiry_time:
            return False

        return True