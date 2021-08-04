from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path("signup/", UserRegisterationView.as_view(), name='sign-up'),
    path('login/', UserLoginView.as_view(), name='login'),
]