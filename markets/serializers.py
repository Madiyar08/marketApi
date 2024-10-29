from rest_framework import serializers
from .models import Market
from django.contrib.auth.models import User

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'  # Или перечислите нужные поля, например: ['id', 'name', 'department_phone', 'city_phone', 'work_schedule']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)