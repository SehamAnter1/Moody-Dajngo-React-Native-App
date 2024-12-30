from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from .serializers import RegisterSerializer, VerifyOtpSerializer, LoginSerializer, ResendOtpSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Registration successful! Check your email for the OTP."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOtpView(APIView):
    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "OTP verified successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "username": user.username,
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login successful."
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResendOtpView(APIView):
    def post(self, request):
        serializer = ResendOtpSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            
            # Fetch the user and generate a new OTP
            user = CustomUser.objects.get(email=email)
            user.generate_otp()
            
            # Send the OTP to the user's email
            send_mail(
                'Your New OTP Code',
                f'Your new OTP code is: {user.otp}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            
            return Response({"message": "A new OTP has been sent to your email."}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
