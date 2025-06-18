#Import datetime 
from datetime import datetime

#get a current date and time # Import datetime

now = datetime.now()
print(now)

#how ti create a date  # Display the current date and time (no formatting)
date = datetime(2025, 6, 12, 18 , 41, 45)
print(date)

#strftime # Display the current date and time following this format: Date: Jan 12, 2032 Time: 14:03
formatted_date = date.strftime("Date %B %d, 2032 Time: %H: %M" )
print(formatted_date)

#create a date from timestamp # Convert this time stamp  into a date and display only the time using this format: 2:30am
# Ton timestamp
timestamp = 1705590204

# Convertir le timestamp en objet datetime
dt = datetime.fromtimestamp(timestamp)

# Extraire l'heure au format 12h avec am/pm
formatted_time = dt.strftime("%I:%M%p")

print(formatted_time)

