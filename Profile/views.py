from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from Profile.models import CustomUser, OTPDevice
from django.contrib.auth import get_user_model
from rest_framework import serializers, permissions
from Profile.Permissions import IsOwnerOrSuperuser
from django.utils import timezone
from Profile.emails import send_otp_email
from Profile.serializer import (CustomTokenObtainPairSerializer, RegisterSerializer, UserSerializer,
                                UpdateUserSerializer, UploadSerializer, UserUpdateSerializerUsingSerializer,
                                GenerateOTPSerializer, ValidateOTPSerializer)
from Profile.generators import OTPGenerator
from Profile.handlers import OTPHandler
from rest_framework_simplejwt.views import TokenObtainPairView

import logging

logger = logging.getLogger("user")


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view for obtaining JWT token pair.
    """
    serializer_class = CustomTokenObtainPairSerializer


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @swagger_auto_schema(operation_description="Register a new user", request_body=UserSerializer)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate tokens
            token_serializer = CustomTokenObtainPairSerializer(data={
                'email': user.email,
                'password': request.data['password']
            })
            token_serializer.is_valid(raise_exception=True)
            tokens = token_serializer.validated_data

            return Response({
                'success': True,
                'message': 'User registered successfully',
                'user': {
                    'id': user.id,
                    'email': user.email
                },
                'tokens': tokens
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListUpdateView(generics.ListAPIView, generics.UpdateAPIView):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.user.is_superuser:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticated(), IsOwnerOrSuperuser()]

    @swagger_auto_schema(operation_description="Retrieve the list of users")
    def get_queryset(self):
        queryset = get_user_model().objects.all()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(id=self.request.user.id)
        return queryset

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UpdateUserSerializer
        return UserSerializer


class UserUpdateSView(generics.UpdateAPIView):
    """
    API endpoint to update a user
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializerUsingSerializer
    permission_classes = [IsAuthenticated]


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    @swagger_auto_schema(operation_description="List uploaded files")
    def list(self, request):
        return Response("GET API")

    @swagger_auto_schema(operation_description="Upload a new file", request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'file_uploaded': openapi.Schema(type=openapi.TYPE_FILE, description='CSV file to upload')
        }
    ))
    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        if not file_uploaded or file_uploaded.content_type != 'text/csv':
            return Response({"error": "Please upload a valid CSV file."}, status=status.HTTP_400_BAD_REQUEST)

        content_type = file_uploaded.content_type
        response = f"POST API: Uploaded {content_type} file successfully"
        return Response(response)


class UserUpdateView(generics.UpdateAPIView):
    """
    API endpoint to update a user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializerUsingSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update user profile
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@swagger_auto_schema(
    method='post',
    operation_description="Generate OTP for the authenticated user",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=[],
        properties={}
    ),
    responses={
        201: openapi.Response(description='OTP generated successfully'),
        400: "Bad Request"
    },
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_otp(request):
    """
    Generate OTP for the authenticated user.
    """
    user = request.user
    otp = OTPGenerator.generate_unique_otp()
    expires_at = timezone.now() + timezone.timedelta(minutes=5)
    OTPDevice.objects.create(user=user, otp=otp, expires_at=expires_at)

    # Assuming send_otp_email is a function that sends the OTP to the user's email
    response = send_otp_email(user.email, otp)
    print('OTP sent successfully')

    return Response({'otp': otp}, status=status.HTTP_201_CREATED)


@swagger_auto_schema(
    method='post',
    operation_description="Validate OTP for the authenticated user",
    request_body=ValidateOTPSerializer,
    responses={
        200: openapi.Response(description='OTP validation successful'),
        400: openapi.Response(description='OTP validation failed')
    },
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def validate_otp(request):
    """
    Validate OTP for the authenticated user.
    """
    serializer = ValidateOTPSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = request.user
    otp_entered = serializer.validated_data['otp']
    stored_otp = OTPHandler.get_otp(user)

    if OTPHandler.validate_otp(otp_entered, stored_otp):
        return Response({'detail': 'OTP validation successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'OTP validation failed'}, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse('Home Page')
