import os
import requests

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

city = input("Enter a city: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "imperial"
}

response = requests.get(url, params=params)

data = response.json()

if response.status_code != 200:
    print("City not found. Please check the city name and try again.")
    exit()

city_name = data["name"]
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]

print()
print(f"Weather for {city_name}")
print(f"Temperature: {temperature}°F")
print(f"Feels like: {feels_like}°F")
print(f"Humidity: {humidity}%")
print(f"Wind speed: {wind_speed} mph")
print(f"Conditions: {description.title()}")