from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
import Profile.serializer
from Profile.serializer import CustomTokenObtainPairSerializer, RegisterSerializer, UserSerializer, UpdateUserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Profile.models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework import serializers


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate tokens
            token_serializer = TokenObtainPairSerializer(data={
                'email': user.email,
                'password': request.data['password']
            })
            token_serializer.is_valid(raise_exception=True)
            tokens = token_serializer.validated_data

            return Response(
                {
                    'success': True,
                    'message': 'User registered successfully',
                    'user': {
                        'id': user.id,
                        'email': user.email
                    },
                    'tokens': tokens
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UpdateUser(generics.UpdateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = CustomUser.objects.all()


def index(request):
    return HttpResponse('Home Page')
