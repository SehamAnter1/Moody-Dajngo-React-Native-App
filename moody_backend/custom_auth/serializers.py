from rest_framework import serializers
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ('email','username','password')
    def create(self, validated_data):
        user = CustomUser(
        email = validated_data['email'],
        username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.generate_otp()
        user.save()
        # Send OTP 
        send_mail(
            'Your OTP Code',
            f'Your OTP code is: {user.otp}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return user
 
        

class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=4)
 
    def validate(self, attrs):
        email = attrs.get('email')
        otp = attrs.get('otp')
        try:
            user = CustomUser.objects.get(email=email)  
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.") 
        verified, message = user.verify_otp(otp)  
        if not verified:  
            raise serializers.ValidationError(message)  
        return attrs 
        
class ResendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = CustomUser.objects.get(email=value)
        except CustomUser.DoesNotExist:        
            raise serializers.ValidationError("User with this email does not exist.")
        if user.is_verified:
            raise serializers.ValidationError("This account is already verified.")
        return value
        
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            raise serializers.ValidationError("Email doesn't exist.")
        
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password.")
        
        if not user.is_verified:
            raise serializers.ValidationError("Please verify your email first.")
        self.user = user
        return attrs
