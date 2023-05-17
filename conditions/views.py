from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from decouple import config
WEATHER_API_KEY = config('WEATHER_API_KEY')

# Create your views here.
@api_view(['GET'])
def search_current_details(request, location):
    url = 'http://api.weatherapi.com/v1/forecast.json?key={}&q={}'.format(WEATHER_API_KEY, location)
    response = requests.get(url)
    data = response.json()
    return Response(data)


@api_view(['GET'])
def search_past_details(request, location, date):
    url = 'http://api.weatherapi.com/v1/history.json?key={}&q={}&date={}'.format(WEATHER_API_KEY,location, date)
    response = requests.get(url)
    data = response.json()
    return Response(data)


@api_view(['GET'])
def search_future_details(request, location, date):
    url = 'http://api.weatherapi.com/v1/forecast.json?key={}&q={}&date={}'.format(WEATHER_API_KEY,location, date)
    response = requests.get(url)
    data = response.json()
    return Response(data)