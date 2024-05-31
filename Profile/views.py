from django.shortcuts import render
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView

import Profile.serializer
from Profile.serializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


def index(request):
    return HttpResponse('Home Page')
