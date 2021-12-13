from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CityName


class CityNameSerializer(ModelSerializer):
    class Meta:
        model = CityName
        fields = '__all__'

