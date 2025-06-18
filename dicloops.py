# Créer un dictionnaire avec 3 pays et leur capitale
countries = {
    "Canada": "Ottawa",
    "France": "Paris",
    "Germany": "Berlin"
}

print("Countries I'd like to visit:")

index = 0
for country, capital_city in countries.items():
  print(f"{index + 1}. {country} (Capital city: {capital_city})")
  index = index + 1