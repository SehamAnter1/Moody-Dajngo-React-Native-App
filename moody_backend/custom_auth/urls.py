from django.urls import path
from .views import RegisterView, VerifyOtpView, LoginView, ResendOtpView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-otp/', VerifyOtpView.as_view(), name='verify_otp'),
    path('login/', LoginView.as_view(), name='login'),
    path('resend-otp/', ResendOtpView.as_view(), name='resend_otp'),
]
