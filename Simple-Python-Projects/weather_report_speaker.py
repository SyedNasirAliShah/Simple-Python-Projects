#WeatherApp

import requests
import json
from win32com.client import Dispatch

def initialize_speaker():
    speaker = Dispatch("SAPI.SpVoice")
    return speaker

def set_rate(speaker, rate=0):
    speaker.Rate = rate

def speakWeather(weather_list):
    speaker = initialize_speaker()
    set_rate(speaker, 2)
    for weather in weather_list:
        print(weather)
        speaker.Speak(weather)

def getCity(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=e8821f6f9fbf4a9aadd90838240707&q={city}"
    response = requests.get(url)
    weather = json.loads(response.text)
    temp_in_cel = f"Temperature in Fahrenheit: {weather["current"]["temp_f"]}"
    temp_in_fahren = f"Temperature in Celsius: {weather["current"]["temp_c"]}"
    wind_in_mph = f"Wind speed mph: {weather["current"]["wind_mph"]}"
    wind_in_kph = f"Wind speed kph: {weather["current"]["wind_kph"]}"
    humidity = f"Humidity: {weather["current"]["humidity"]}"
    heat_index_cel = f"Heat Index in Celsius: {weather["current"]["heatindex_c"]}"
    heat_index_fahren = f"Heat Index in Fahrenheit: {weather["current"]["heatindex_f"]}"
    weather_list = [temp_in_cel, temp_in_fahren, wind_in_mph,wind_in_kph, humidity, heat_index_cel, heat_index_fahren]
    speakWeather(weather_list)

if __name__ == "__main__":
    city = input("Enter the city: ")
    getCity(city)

