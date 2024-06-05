from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from Profile.models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer, FileField


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        print(f'Token :{token}')
        print(f' username: {user.username}, email: {user.email}')
        return token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['email'], password=validated_data['password'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address']

    def get_fields(self):
        # Get the default fields from the superclass
        fields = super().get_fields()

        # Make email, username, and password read-only
        fields['email'].read_only = True
        fields['username'].read_only = True
        return fields


class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']

    def update(self, instance, validated_data):
        # Update phone_number and address
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


# class AudioTextSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AudioText
#         fields = ('audio_file', 'text')
