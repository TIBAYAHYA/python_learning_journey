import sys,requests
import json
OpenWeather_API_token = input("please enter your api token \n")
if len(sys.argv) < 2:
    location = " ".join(sys.argv[1:])
location = "London,uk"
url = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+OpenWeather_API_token

response = requests.get(url)
weather_jasoned = json.loads(response.text)


main_weather = weather_jasoned['weather'][0]['main']
description = weather_jasoned['weather'][0]['description']
temperature = weather_jasoned['main']['temp']
feels_like = weather_jasoned['main']['feels_like']
humidity = weather_jasoned['main']['humidity']
pressure = weather_jasoned['main']['pressure']
wind_speed = weather_jasoned['wind']['speed']
wind_deg = weather_jasoned['wind']['deg']
visibility = weather_jasoned['visibility']
sunrise = weather_jasoned['sys']['sunrise']
sunset = weather_jasoned['sys']['sunset']

print(f"Current weather in {location}:")
print(f"{main_weather} - {description}")
print(f"Temperature: {temperature}K (Feels like: {feels_like}K)")
print(f"Humidity: {humidity}%")
print(f"Pressure: {pressure} hPa")
print(f"Wind: {wind_speed} m/s at {wind_deg} degrees")
print(f"Visibility: {visibility} meters")
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

