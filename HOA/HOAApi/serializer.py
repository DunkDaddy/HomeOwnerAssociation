from rest_framework import serializers
from .models import *

class BeboerSerializer(serializers.Serializer):
    class Meta:
        model = Beboer
        fields = '__all__'


class LocationSerializer(serializers.Serializer):
    class Meta:
        model = Location
        fields = '__all__'


class ReglerSerializer(serializers.Serializer):
    class Meta:
        model = Regler
        fields = '__all__'


class AndmeldelseSerializer(serializers.Serializer):
    class Meta:
        model = Andmeldelse
        fields = '__all__'
