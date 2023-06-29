# weather/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import WeatherForecast
import requests
import datetime

OPENWEATHERMAP_API_KEY = 'a8fb7a7d3fc6fbc63c60c07f6d114787'
DATA_FRESHNESS_THRESHOLD = datetime.timedelta(minutes=10)

def get_weather_forecast(request):
    lat = float(request.GET.get('lat', 0))
    lon = float(request.GET.get('lon', 0))
    detailing_type = request.GET.get('detailing_type', '')

    # Check if data exists in local DB and within the freshness threshold
    forecast = WeatherForecast.objects.filter(
        lat=lat,
        lon=lon,
        detailing_type=detailing_type,
        timestamp__gte=timezone.now() - DATA_FRESHNESS_THRESHOLD
    ).first()

    if forecast:
        return JsonResponse(forecast.weather_data)

    # Data not found or expired, fetch from OpenWeatherMap API
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHERMAP_API_KEY}'
    response = requests.get(url)
   

    if response.status_code == 200:
        weather_data = response.json()
        

        # Save the new data to the local DB
        forecast = WeatherForecast(
            lat=lat,
            lon=lon,
            detailing_type=detailing_type,
            timestamp=timezone.now(),
            weather_data=weather_data
        )
        forecast.save()
        
        return JsonResponse(weather_data)

    return JsonResponse({'error': 'Failed to fetch weather data'})

def weather_forecast(request):
    return render(request, 'weather/forecast.html')
