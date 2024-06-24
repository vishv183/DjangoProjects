from rest_framework import serializers
from laptop.models import Laptop


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'


class UploadSerializer(serializers.Serializer):
    file_uploaded = serializers.FileField()

    def validate_file_uploaded(self, value):
        # Custom validation for the uploaded file, if needed
        if value.content_type != 'text/csv':
            raise serializers.ValidationError("Only CSV files are allowed.")
        return value