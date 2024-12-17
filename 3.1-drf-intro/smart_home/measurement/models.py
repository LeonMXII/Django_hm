from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчик')

    def __str__(self):
        return f'{self.sensor.name} - {self.temperature}°C ({self.date_time})'





