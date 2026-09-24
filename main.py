from datetime import datetime
import requests
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()

api_key = os.getenv("API_KEY")

def get_weather_merignac():
    return requests.get(
    f'http://api.openweathermap.org/data/2.5/forecast?lat=44.8448769&lon=-0.656358&lang=fr&units=metric&appid={api_key}')

def get_weather_toulouse():
    return requests.get(
    f'http://api.openweathermap.org/data/2.5/forecast?lat=43.604652&lon=1.444209&lang=fr&units=metric&appid={api_key}')

def get_weather_stgeours():
    return requests.get(
    f'http://api.openweathermap.org/data/2.5/forecast?lat=48.862725&lon=2.287592&lang=fr&units=metric&appid={api_key}')


def display_weather_by_city(city, response):
    print(f'--- La Météo à {city} (à partir de demain) ---')
    data = response.json()

    daily_forecasts = defaultdict(list)

    for item in data['list']:
        date_str = item['dt_txt'].split(' ')[0]
        daily_forecasts[date_str].append(item)

    print("")

    # On récupère toutes les dates triées par ordre chronologique
    sorted_dates = sorted(daily_forecasts.keys())

    # On ignore le premier jour (index 0, qui est incomplet) et on commence au lendemain (index 1)
    for date_str in sorted_dates[1:]:
        items = daily_forecasts[date_str]

        temp_min_day = round(min(i['main']['temp_min'] for i in items))
        temp_max_day = round(max(i['main']['temp_max'] for i in items))

        date_obj = datetime.strptime(date_str, '%Y-%m-%d')

        print(f"Date : {date_obj.strftime('%d/%m/%Y')}")
        print(f"Temperature min : {temp_min_day}°C")
        print(f"Temperature max : {temp_max_day}°C")
        print("-" * 25)
    print("")

if __name__ == '__main__':

    display_weather_by_city("Mérignac", get_weather_merignac())
    display_weather_by_city("Toulouse", get_weather_toulouse())
    display_weather_by_city("Saint-Geours-de-Maremne", get_weather_stgeours())

