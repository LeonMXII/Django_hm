from django.urls import path

from measurement.views import SensorListCreateView, SensorRetrieveUpdateView, MeasurementCreateView

# TODO: зарегистрируйте необходимые маршруты

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor_create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor_update'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement_create'),
]
