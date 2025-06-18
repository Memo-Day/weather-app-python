# Exercise 1
weather = {
  "city":"Lisbon",
  "country":"Portugal",
  "temperature": 17.94,
  "humidity":77
}
print(f"It is {round(weather['temperature'])}ºC ({round(weather['temperature'] * 9 / 5 + 32)}ºF) in {weather['city']}, {weather['country']}, the humidity level")
# Display the weather in Lisbon such as:
# It is 18ºC (64ºF) in Lisbon, Portugal, the humidity level is 77%.


# Exercise 2
forecast = {
  "city": "Lisbon",
  "country": "Portugal",
  "daily": [17.76, 13.08, 12.14, 11.25, 14.29]
}

print(f"The forecast for {forecast['city']}, {forecast['country']} for the next 5 days is:")

for i, temp_celsius in enumerate(forecast["daily"], start=1):
    temp_c_rounded = round(temp_celsius)
    temp_f = round(temp_celsius * 9 / 5 + 32)
    print(f"Day {i}: {temp_c_rounded}ºC ({temp_f}ºF)")
# Display the forecast in Lisbon such as:
# The forecast for Lisbon, Portugal for the next 5 days is:
# Day 1: 18ºC
# Day 2: 13ºC
# Day 3: 12ºC
# Day 4: 11ºC
# Day 5: 14ºC




