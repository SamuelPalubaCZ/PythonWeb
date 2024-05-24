import requests
from flask import Flask
import json

def weather_dowland(location,soubor="weather.json"):
    #we gonna call open weather api and dowland json of actual wearher
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': 'e7704bc895b4a8d2dfd4a29d404285b6'
    }
    response = requests.get(url, params=params)
    weather = response.json()
    #we need to dowland weather into json called weather.json
    with open(soubor, 'w') as file:
        json.dump(weather, file)
    return soubor

def weather_tempature(soubor="weather.json"):
    #we gonna read json file and return tempature
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['main']['temp']

def weather_description(soubor="weather.json"):
    #we gonna read json file and return description
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['weather'][0]['description']

def weather_wind_speed(soubor="weather.json"):
    #we gonna read json file and return wind speed
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['wind']['speed']

def weather_wind_deg(soubor="weather.json"):
    #we gonna read json file and return wind degree
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['wind']['deg']

def weather_humidity(soubor="weather.json"):
    #we gonna read json file and return humidity
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['main']['humidity']

def weather_pressure(soubor="weather.json"):
    #we gonna read json file and return pressure
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['main']['pressure']

def weather_visibility(soubor="weather.json"):
    #we gonna read json file and return visibility
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['visibility']

def weather_sunrise(soubor="weather.json"):
    #we gonna read json file and return sunrise
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['sys']['sunrise']

def weather_sunset(soubor="weather.json"):
    #we gonna read json file and return sunset
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['sys']['sunset']

def weather_country(soubor="weather.json"):
    #we gonna read json file and return country
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['sys']['country']

def weather_city(soubor="weather.json"):
    #we gonna read json file and return city
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['name']

def weather_icon(soubor="weather.json"):
    #we gonna read json file and return icon
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['weather'][0]['icon']

def weather_main(soubor="weather.json"):
    #we gonna read json file and return main
    with open(soubor, 'r') as file:
        weather = json.load(file)
    return weather['weather'][0]['main']

def weather_description(soubor="weather.json"):
    #we gonna read json file and return description
    with open(soubor, 'r') as file:
        pass
    
#weather_dowland("Warsaw")
#weather_tempature("weather.json")
print(weather_tempature(weather_dowland("Warsaw")))
