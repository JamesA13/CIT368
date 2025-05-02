import requests
import config
from valid import Valid
import time
import sys

def get_zip():
    user_input = input("Enter a 5-digit ZIP Code: ")
    while (not Valid.validate_zip(user_input)):
        user_input = input("Input error. Please enter a ZIP in the format of #####: ")
    return user_input

def get_weather(zip, key):
    #Initial request from API
    print("Fetching weather forecast...")
    forecast = requests.get(
        f"https://api.tomorrow.io/v4/weather/forecast?location={zip}%20US&units=imperial&apikey={key}"
    )

    #Verify response from API and retry connection up to 3 additional times before quitting with an error msg
    retry = 0
    while(not Valid.validate_response_code(forecast.status_code) and retry < 3):
        forecast = requests.get(
            f"https://api.tomorrow.io/v4/weather/forecast?location={zip}%20US&units=imperial&apikey={key}"
        )
        time.sleep(1)
        retry += 1
    if(retry > 2):
        print("API Error. Please verify your ZIP code and API Key, or contact an administrator.\nExiting program...")
        sys.exit()
    return forecast

def weather_code(code):
    match code:
        case 0:     return "Unknown"
        case 1000:  return "Clear, Sunny"
        case 1100:  return "Mostly Clear"
        case 1101:  return "Partly Cloudy"
        case 1102:  return "Mostly Cloudy"
        case 1001:  return "Cloudy"
        case 2000:  return "Fog"
        case 2100:  return "Light Fog"
        case 4000:  return "Drizzle"
        case 4001:  return "Rain"
        case 4200:  return "Light Rain"
        case 4201:  return "Heavy Rain"
        case 5000:  return "Snow"
        case 5001:  return "Flurries"
        case 5100:  return "Light Snow"
        case 5101:  return "Heavy Snow"
        case 6000:  return "Freezing Drizzle"
        case 6001:  return "Freezing Rain"
        case 6200:  return "Light Freezing Rain"
        case 6201:  return "Heavy Freezing Rain"
        case 7000:  return "Ice Pellets"
        case 7101:  return "Heavy Ice Pellets"
        case 7102:  return "Light Ice Pellets"
        case 8000:  return "Thunderstorm"
        case _:     return "Unknown"

zip_code = get_zip()

user_forecast = get_weather(zip_code, config.key)

for i in range(0, 3):
    conditions = user_forecast.json()["timelines"]["daily"][i]["values"]["weatherCodeMax"]
    max_temp = str(user_forecast.json()["timelines"]["daily"][i]["values"]["temperatureMax"])
    min_temp = str(user_forecast.json()["timelines"]["daily"][i]["values"]["temperatureMin"])
    if i == 0:
        print("Today's weather is: " + weather_code(conditions) + ", with a high of " + max_temp + " degrees and low of " + min_temp + " degrees.")
    elif i == 1:
        print("Tomorrow's weather is: " + weather_code(conditions) + ", with a high of " + max_temp + " degrees and low of " + min_temp + " degrees.")
    elif i == 2:
        print("Overmorrow's weather is: " + weather_code(conditions) + ", with a high of " + max_temp + " degrees and low of " + min_temp + " degrees.")
    i += 1
