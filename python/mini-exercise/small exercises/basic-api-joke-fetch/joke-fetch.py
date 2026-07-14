import requests
import json

# Free joke API
response = requests.get("https://official-joke-api.appspot.com/random_joke")


if response.status_code == 200:
    joke = response.json()
    print(f"Joke: {joke['setup']}")
    print(f"Punchline: {joke['punchline']}")
else:
    print(f"Error: {response.status_code}")