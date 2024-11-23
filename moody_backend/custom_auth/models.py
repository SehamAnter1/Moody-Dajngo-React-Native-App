from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    otp = models.EmailField(max_length=4, blank=True, null=True)
    is_verified = models.BooleanField(default=False)  
    otp_created_at = models.DateTimeField(null=True, blank=True) 
    
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username']
    
    # auto generate otp when user created
    def generate_otp(self):
        self.otp = str(random.randint(1000,9999))
        self.otp_created_at = timezone.now()
        self.save()
    # validate otp
    def verify_otp(self,otp):
        if self.otp==otp and self.otp_created_at:
            if timezone.now()-self.otp_created_at <= timezone.timedelta(minutes=5):
                self.is_verified = True
                self.otp_created_at = None
                self.otp=None
                self.save()
                return True, "OTP verified successfully."
            return False, "OTP has expired."
        return False, "Invalid OTP."
    
        
