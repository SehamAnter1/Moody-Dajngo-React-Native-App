from django.urls import path
from .views import register,verify_otp,login_view,resend_otp


urlpatterns = [
    path('register/', register, name='register'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('login/', login_view, name='login'),
    path('resend-otp/', resend_otp, name='resend_otp'),

    ]