from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView



class SensorListCreateView(ListCreateAPIView):
    sensor = Sensor.objects.all()
    ser = SensorSerializer



class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    sensor = Sensor.objects.all()
    ser = SensorDetailSerializer



class MeasurementCreateView(CreateAPIView):
    meas = Measurement.objects.all()
    ser = MeasurementSerializer

