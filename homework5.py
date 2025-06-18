import requests
from rich import print

city = input("Enter a city: ")
city = city.capitalize()

api_key = "749b4a3937d79a07ao7fd73bd32t1f04"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

response = requests.get(api_url)
weather = response.json()

print(weather)

temperature = weather["temperature"]["current"]
country = weather["country"]

print(f"It is  {round(temperature)}°C in {city}, {country}.")
# It is currently 10ºC in Tokyo, Japan.
