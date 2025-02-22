from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)

class Measurement(models.Model):
    id_sensor = models.CharField(max_length=150)
    temperature = models.FloatField(max_length=150)
    date_time = models.DateTimeField(auto_now_add=True)

