import os
import requests

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def get_weather(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }

    response = requests.get(url, params=params)

    return response


def display_weather(data):
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


def main():
    city = input("Enter a city: ")

    response = get_weather(city, api_key)
    data = response.json()

    if response.status_code != 200:
        print("City not found. Please check the city name and try again.")
        return

    display_weather(data)


if __name__ == "__main__":
    main()