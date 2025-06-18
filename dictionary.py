# Créer un dictionnaire avec des pays comme clés et les capitales comme valeurs
countries = {
    "Portugal": "Lisbon",
    "France": "Paris",
    "Spain": "Madrid"
}

# Ajouter un nouveau pays
countries["Sweden"] = "Stockholm"

# Afficher le dictionnaire
print(countries)

# Remove your least favorite country from the dictionary
del countries["Portugal"]
print(countries)

# Add another country you'd like to visit 
countries["Japan"] = "Tokyo"
# Print out the dictionary
print(countries)
# Display the capital of each country (one at a time, don't use a loop)
print(f"The capital of France is {countries['France']}.")
print(f"The capital of Spain is {countries['Spain']}.")
print(f"The capital of Sweden is {countries['Sweden']}.")
print(f"The capital of Japan is {countries['Japan']}.")

