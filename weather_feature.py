import requests
from datetime import datetime
import pyttsx3
import json
# 3c84fa341a5c80303108ec0ce3ba4ca1

engine = pyttsx3.init()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Info to show: Temperature, Humidity, Wind speed, weather description


def weather_forecast(city):
    try:
        user_api = "da7e8fa5805bffca5b90637d45bf32bd"
        location = city

        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
            location + "&appid="+user_api

        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data["cod"] == "404":
            print(f"{location} is an invalid, city name please try again")
        else:
            temperature = ((api_data["main"]["temp"])-273.15)
            weather_description = api_data["weather"][0]["description"]
            wind_speed = api_data["wind"]["speed"]
            humidity = api_data["main"]["humidity"]
            pressure = api_data["main"]["pressure"]
            date_time = datetime.now().strftime("%d %B %Y ||  %I:%M:%S %p")

        print("---------------------------------------------------------")
        print(
            f"Information/Stats on Weather of {location}. Time: {date_time} ")
        print("---------------------------------------------------------")

        print(f"The Current Temperature is {temperature:.2f}°C")
        print(f"The Current Weather condition is {weather_description}")
        print(f"The Current Humidty is {humidity}%")
        print(f"The Current Wind Speed is {wind_speed} kmph")
        print(f"The Current Atmospheric pressure is {pressure}(in hPa unit) ")
        engine.say(
            f"The current weather condition in {location} is {weather_description} with a temperature of {temperature:.2f} degree celsius, humidity of {humidity} percentage and wind speed of {wind_speed} kilometres per hour. The pressure is {pressure}")
        engine.runAndWait()

    except Exception as e:
        print(f"Error: {e}")
