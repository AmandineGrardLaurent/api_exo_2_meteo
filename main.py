from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

weather_merignac = requests.get(
    f'http://api.openweathermap.org/data/2.5/forecast?lat=44.8448769&lon=-0.656358&lang=fr&units=metric&appid={api_key}')
weather_toulouse = requests.get(
    f'http://api.openweathermap.org/data/2.5/forecast?lat=43.604652&lon=1.444209&lang=fr&units=metric&appid={api_key}')
weather_stgeours = requests.get(
    f'http://api.openweathermap.org/data/2.5/forecast?lat=48.862725&lon=2.287592&lang=fr&units=metric&appid={api_key}')

if __name__ == '__main__':
    #print(weather_merignac.json()['list'])

    print('--- La Méthode à Mérignac ---')
    for item in weather_merignac.json()['list']:
        print(f'Date : {datetime.fromtimestamp(item['dt'])}')
        print(f'Temperature : {item['main']['temp']}°C')
        print(f'Temperature min : {item['main']['temp_min']}°C')
        print(f'Temperature max : {item['main']['temp_max']}°C')

    print('--- La Méthode à Toulouse ---')
    for item in weather_toulouse.json()['list']:
        print(f'Date : {datetime.fromtimestamp(item['dt'])}')
        print(f'Temperature : {item['main']['temp']}°C')
        print(f'Temperature min : {item['main']['temp_min']}°C')
        print(f'Temperature max : {item['main']['temp_max']}°C')

    print('--- La Méthode à Saint-Geours-de-Maremne ---')
    for item in weather_stgeours.json()['list']:
        print(f'Date : {datetime.fromtimestamp(item['dt'])}')
        print(f'Temperature : {item['main']['temp']}°C')
        print(f'Temperature min : {item['main']['temp_min']}°C')
        print(f'Temperature max : {item['main']['temp_max']}°C')
