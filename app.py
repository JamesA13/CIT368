import requests
import config
from valid import Valid
import time
from log import Log

def get_zip():
    user_input = input("Enter a 5-digit ZIP Code: ")
    while (not Valid.validate_zip(user_input)):
        user_input = input("Input error. Please enter a ZIP in the format of #####: ")
    return user_input

def get_weather(zip, key):
    print("Fetching weather forecast...")
    time.sleep(1) # Enforce a 1-second wait before any request to avoid rate-limiting the user
    forecast = requests.get(
        f"https://api.tomorrow.io/v4/weather/forecast?location={zip}%20US&units=imperial&apikey={key}"
    )
    return forecast
    
def print_forecast(forecast):
    print("Today's weather is: " + 
        weather_code(forecast.json()["timelines"]["daily"][0]["values"]["weatherCodeMax"]) # Weather conditions code passed through the interpreting method
        + ", with a high of " + str(forecast.json()["timelines"]["daily"][0]["values"]["temperatureMax"]) # Max Temp of the day
        + " degrees and low of " + str(forecast.json()["timelines"]["daily"][0]["values"]["temperatureMin"]) # Min Temp of the day
        + " degrees.")
    
    print("Tomorrow's weather is: " +  
        weather_code(forecast.json()["timelines"]["daily"][1]["values"]["weatherCodeMax"])
        + ", with a high of " + str(forecast.json()["timelines"]["daily"][1]["values"]["temperatureMax"])
        + " degrees and low of " + str(forecast.json()["timelines"]["daily"][1]["values"]["temperatureMin"])
        + " degrees.")
    
    print("Overmorrow's weather is: " + 
        weather_code(forecast.json()["timelines"]["daily"][2]["values"]["weatherCodeMax"])
        + ", with a high of " + str(forecast.json()["timelines"]["daily"][2]["values"]["temperatureMax"])
        + " degrees and low of " + str(forecast.json()["timelines"]["daily"][2]["values"]["temperatureMin"]) 
        + " degrees.")

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

##################################

key = config.key
zip_code = get_zip()
user_forecast = get_weather(zip_code, key)

# Verify response from API and retry connection up to 3 additional times before quitting with an error msg
if(Valid.validate_response_code(user_forecast.status_code)):
    print_forecast(user_forecast)
    Log.log(zip_code, user_forecast.status_code)
else:
    retry = 1
    while(not Valid.validate_response_code(user_forecast.status_code) and retry < 3):
        print("API error. Retrying...")
        user_forecast = get_weather(zip_code, key)
        retry += 1
    if(Valid.validate_response_code(user_forecast.status_code)):
        print_forecast(user_forecast)
        Log.log(zip_code, user_forecast.status_code)
    else:
        print("API Error. Please verify your ZIP code and API Key, or contact an administrator.\nTo avoid rate-limiting your API key, the program will now exit.")
        Log.log(zip_code, user_forecast.status_code)