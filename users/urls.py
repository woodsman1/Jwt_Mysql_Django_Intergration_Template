from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("signup/", UserRegisterationView.as_view(), name='sign-up'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("refresh/", TokenRefreshView.as_view(), name='refresh'),
]