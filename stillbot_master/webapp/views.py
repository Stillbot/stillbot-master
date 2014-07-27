from rest_framework import viewsets
from .serializers import ThermistorSerializer, TemperatureSerializer
from .models import Thermistor, Temperature
from django.contrib.auth.models import User, Group
from rest_framework import generics


class ThermistorViewSet(viewsets.ModelViewSet):
    queryset = Thermistor.objects.all()
    serializer_class = ThermistorSerializer


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    filter_fields = ('thermistor', 'thermistor__index', 'created_on', )


class UserViewSet(viewsets.ModelViewSet):
    model = User


class GroupViewSet(viewsets.ModelViewSet):
    model = Group
