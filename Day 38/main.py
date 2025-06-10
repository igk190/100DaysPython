import os
import requests

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
HOST_DOMAIN = "https://trackapi.nutritionix.com"
NATTY_EXERCISE_ENDPOINT = "v2/natural/exercise"
full_endpoint = f"{HOST_DOMAIN}/{NATTY_EXERCISE_ENDPOINT}"

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json",
}

params = {
    "query": input("What exercises did you do?") # only param required
}

response = requests.post(url=full_endpoint, headers=headers, json=params)
print(response.text)

""" Learnings

1. Unsure where/how to start? Look at requests module on w3schools. 
The hints in the course exercise pointed toward:

- reading the API documentation (of course) 
- request headers
- POST requests

Syntax for POST request:

requests.post(url, data={key: value}, json={key: value}, args)
Aka: we can continye to insert the data and json in objects like in earlier exercises.

Ex: requests.post(url, data = myobj, timeout=2.50)

Here, of exercise params, only query is required.

"""



