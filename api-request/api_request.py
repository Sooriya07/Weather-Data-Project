import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=Chennai"

def fetch_data():

    print("Fetching weather data from the Weatherstack API...")

    try:

        response = requests.get(api_url)
        response.raise_for_status() 
        print("API request successful!")
        return response.json()

    except requests.exceptions.RequestException as e:

        print(f"API request failed: {e}")
        raise

#print(fetch_data())

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Chennai, India', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Chennai', 'country': 'India', 'region': 'Tamil Nadu', 'lat': '13.083', 'lon': '80.283', 'timezone_id': 'Asia/Kolkata', 'localtime': '2026-10-16 20:43', 'localtime_epoch': 1792183380, 'utc_offset': '5.50'}, 'current': {'observation_time': '03:13 PM', 'temperature': 28, 'weather_code': 296, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0033_cloudy_with_light_rain_night.png'], 'weather_descriptions': ['Light rain'], 'astro': {'sunrise': '05:59 AM', 'sunset': '05:50 PM', 'moonrise': '10:41 AM', 'moonset': '10:07 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 26}, 'air_quality': {'co': '594', 'no2': '12.5', 'o3': '47', 'so2': '5.9', 'pm2_5': '8.5', 'pm10': '9.4', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 8, 'wind_degree': 122, 'wind_dir': 'ESE', 'pressure': 1010, 'precip': 1.5, 'humidity': 76, 'cloudcover': 100, 'feelslike': 32, 'uv_index': 0, 'visibility': 9, 'is_day': 'no'}}