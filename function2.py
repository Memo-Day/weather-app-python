def meteo(city, temperature):
 city = input("Enter the name of the city: ").capitalize()
temperature = int(input(f"Enter the temperature (°C) in {city}: "))

  meteo(city, temperature)
  print(f"The temperature in {city} is currently {temperature} degrees")


# Appels de la fonction avec des valeurs différentes
meteo("London", 7)
meteo("Stockholm", -2)
