from typing import ContextManager

from .models import City
from django.shortcuts import render
import requests

from .form import CityForm

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=730a0eb4ccac02c8c476456d68ea2553'
    # city = 'India'
    # print(r)
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city':city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']

        }
        weather_data.append(city_weather)

    print(weather_data)

    # print(city_weather)
    context = {'weather_data' : weather_data, 'form' : form}

    return render(request,'weather/weather.html',context)

  