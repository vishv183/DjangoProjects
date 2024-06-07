from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import Profile.serializer
from Profile.serializer import (CustomTokenObtainPairSerializer, RegisterSerializer, UserSerializer, \
                                UpdateUserSerializer, UploadSerializer, UserUpdateSerializerUsingSerializer,
                                GenerateOTPSerializer, \
                                ValidateOTPSerializer)
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Profile.models import CustomUser, OTPDevice
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.views import APIView
from Profile.Permissions import IsOwnerOrSuperuser
from django.test import TestCase
from rest_framework.permissions import IsAuthenticated
from Profile.generators import OTPGenerator
from Profile.handlers import OTPHandler
from django.utils import timezone
from Profile.emails import send_otp_email
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


# class UserListView(generics.ListAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
#
#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return get_user_model().objects.all()
#         else:
#             return CustomUser.objects.filter(id=self.request.user.id)
#
#
# class UpdateUser(generics.UpdateAPIView):
#     serializer_class = UpdateUserSerializer
#     queryset = CustomUser.objects.all()
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserListUpdateView(generics.ListAPIView, generics.UpdateAPIView):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.user.is_superuser:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticated(), IsOwnerOrSuperuser()]

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(id=self.request.user.id)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UpdateUserSerializer
        return UserSerializer


class UserUpdateSView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializerUsingSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Assume the user is updating their own profile
        return self.request.user


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)


class UserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializerUsingSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_otp(request):
    user = request.user
    otp = OTPGenerator.generate_unique_otp()
    expires_at = timezone.now() + timezone.timedelta(minutes=5)
    OTPDevice.objects.create(user=user, otp=otp, expires_at=expires_at)
    response = send_otp_email(user.email, otp)
    print('otp send successfully')
    # Send OTP to user via email/sms etc.
    return Response( status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def validate_otp(request):
    serializer = ValidateOTPSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = request.user
    otp_entered = serializer.validated_data['otp']
    stored_otp = OTPHandler.get_otp(user)

    if OTPHandler.validate_otp(otp_entered, stored_otp):
        # OTP validation successful
        return Response({'detail': 'OTP validation successful'}, status=status.HTTP_200_OK)
    else:
        # OTP validation failed
        return Response({'detail': 'OTP validation failed'}, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse('Home Page')
