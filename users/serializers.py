from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from .models import CustomUser

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = {'first_name', 'last_name'}


class UserRegistrationSerializer(serializers.ModelSerializer):

    # profile = UserSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # profile_data = validated_data.pop('profile')
        user = CustomUser.objects.create_user(**validated_data) # here profile is included in validated data. keep an eye if error occures.
        return user


class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=260)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=260, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        
        if user is None:
            raise serializers.ValidationError('Incorrect Credentials')
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('Incorrect Credentials')
        
        response = {
            'email': user.email,
            'token': jwt_token
        }
        return response
