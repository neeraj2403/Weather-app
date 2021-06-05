from typing import ContextManager
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=730a0eb4ccac02c8c476456d68ea2553'
    city = 'India'
    r = requests.get(url.format(city)).json()
    # print(r)

    city_weather = {
        'city':city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']

    }


    # print(city_weather)
    context = {'city_weather' : city_weather}

    return render(request,'weather/weather.html',context)

  