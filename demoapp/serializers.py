from rest_framework import serializers
from .models import Restaurants

class Resserializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = '__all__'
