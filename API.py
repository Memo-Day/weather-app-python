# Install and import 'requests'


import requests
# Get and print out the response from this URL https://jsonplaceholder.typicode.com/photos/1
response = requests.get("https://jsonplaceholder.typicode.com/photos/1")

print(response)

# Convert the response to JSON
todo = response.json()
# Print out the title and thumbnail url of the photo from the response
print(todo['title'])
print(todo['thumbnailUrl'])