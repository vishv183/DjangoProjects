from rest_framework import serializers
from Watches.models import Watch


class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = '__all__'

