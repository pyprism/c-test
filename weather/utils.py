import requests
from proj.settings import OPENWEATHER_API
from weather.models import CityName
from django.core.cache import cache


def get_current_weather(city_pk):
    city_name = CityName.objects.get_city_by_pk(city_pk)
    if cache.get(city_name['name']):
        print('Данные из кэша')
        return cache.get(city_name['name'])
    else:
        print('Нет в кэше')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name['name']}&appid={OPENWEATHER_API}&units=metric"
        resp = requests.get(url)
        if resp.status_code == 200:
            response = resp.json()
            temp = response['main']['temp']
            humidity = response['main']['humidity']
            feels_like = response['main']['feels_like']
            data = {"city": city_name['name'], "temperature": temp, "humidity": humidity, "feels_like": feels_like}
            cache.set(city_name['name'], data, timeout=300)  # cache for 5 minutes
            return data
        else:
            return None


