
from django.http import response
from django.shortcuts import get_list_or_404, render

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .models import CustomUser
from .serializers import *


class UserRegisterationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 1,
            'status_code': status_code,
            'message': 'User Registered Successfully',
        }
        return Response(response, status=status_code)

class UserLoginView(RetrieveAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'sucess': 1,
            'status_code': status.HTTP_200_OK,
            'message': 'Login in succesfull',
            'refresh': serializer.data['refresh'],
            'token': serializer.data['access'],
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)