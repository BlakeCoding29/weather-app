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

print(response.json())