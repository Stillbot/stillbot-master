from rest_framework import serializers

from .models import Thermistor, Temperature

class ThermistorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thermistor
        fields = ('index', 'model', 'name', 'url')


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    temp = serializers.Field('temp')
    created_on = serializers.Field('created_on')

    class Meta:
        model = Temperature
        fields = ('thermistor', 'temp', 'created_on', 'url')
