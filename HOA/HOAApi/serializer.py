from rest_framework import serializers
from .models import *


class BeboerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beboer
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class ReglerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regler
        fields = '__all__'


class AndmeldelseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Andmeldelse
        fields = '__all__'
