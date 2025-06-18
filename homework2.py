city = input("Enter the name of a city: ")
temperature = input(f"Enter the temperature in {city}: ")

if city and temperature:
  temperature = int(temperature)

  if temperature > 20:
    print(
        f"It is currently warm in {city} with a temperature of {temperature} degrees."
    )
  elif temperature > 10:
    print(
        f"It is currently chilly in {city} with a temperature of {temperature} degrees."
    )
  else:
    print(
        f"It is currently cold in {city} with a temperature of {temperature} degrees."
    )
else:
  print("Please try again and enter a city and temperature")
