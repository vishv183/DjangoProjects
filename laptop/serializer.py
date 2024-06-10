from rest_framework import serializers
from laptop.models import Laptop


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'
