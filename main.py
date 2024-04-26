import requests
import flask
import json
app = flask.Flask(__name__)
#now we gonna iniciate web server
@app.route('/')
def weather_dowland(location):
    #we gonna call open weather api and dowland json of actual wearher
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': 'e7704bc895b4a8d2dfd4a29d404285b6'
    }
    response = requests.get(url, params=params)
    weather = response.json()
    #we need to dowland weather into json called weather.json
    with open('weather.json', 'w') as file:
        json.dump(weather, file)
def weather_tempature():
    #we gonna read json file and return tempature
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['main']['temp']
def weather_description(json):
    #we gonna read json file and return description
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['weather'][0]['description']
def weather_wind_speed():
    #we gonna read json file and return wind speed
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['wind']['speed']

def weather_wind_deg():
    #we gonna read json file and return wind degree
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['wind']['deg']

def weather_humidity():
    #we gonna read json file and return humidity
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['main']['humidity']

def weather_pressure():
    #we gonna read json file and return pressure
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['main']['pressure']

def weather_visibility():
    #we gonna read json file and return visibility
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['visibility']

def weather_sunrise():
    #we gonna read json file and return sunrise
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['sys']['sunrise']

def weather_sunset():
    #we gonna read json file and return sunset
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['sys']['sunset']

def weather_country():
    #we gonna read json file and return country
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['sys']['country']

def weather_city():
    #we gonna read json file and return city
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['name']

def weather_icon():
    #we gonna read json file and return icon
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['weather'][0]['icon']

def weather_main():
    #we gonna read json file and return main
    with open('weather.json', 'r') as file:
        weather = json.load(file)
    return weather['weather'][0]['main']
weather_dowland("Warsaw")
weather_tempature()
print(weather_tempature())

