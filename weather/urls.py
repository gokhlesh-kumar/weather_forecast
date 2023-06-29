# weather/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('weather-forecast/', views.get_weather_forecast, name='get_weather_forecast'),
    path('', views.weather_forecast, name='weather_forecast'),
]
