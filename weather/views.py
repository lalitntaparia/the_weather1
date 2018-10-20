

# Create your views here.

#the_weather/weather/views.py

from django.shortcuts import render
import requests




def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=20edd749e144676c0b6b8afa8ca10dce'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    return render(request, 'weather/index.html') #returns the index.html template
