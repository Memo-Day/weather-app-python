import requests
from rich import print

city = "Tokyo"


api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

response = requests.get(api_url)
weather = response.json()

print(weather)

temperature = weather["temperature"]["current"]
humidity = weather["temperature"]["humidity"]
country = weather["country"]

print(f"It is currently  {round(temperature)}°C in {city}, {country} and the humidity level is {humidity}%")
#It is currently 10ºC in Tokyo, Japan and the humidity level is 40%
 