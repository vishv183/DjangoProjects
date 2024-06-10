from rest_framework import serializers
from laptop.models import GamingLaptop


class GamingLaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamingLaptop
        fields = '__all__'
