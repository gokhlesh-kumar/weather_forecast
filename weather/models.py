# weather/models.py

from django.db import models

class WeatherForecast(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    detailing_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    weather_data = models.JSONField()
