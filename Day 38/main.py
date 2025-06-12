import os
import requests
import datetime as dt
import json

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
HOST_DOMAIN = "https://trackapi.nutritionix.com"
NATTY_EXERCISE_ENDPOINT = "v2/natural/exercise"
NATTY_FULL_ENDPOINT = f"{HOST_DOMAIN}/{NATTY_EXERCISE_ENDPOINT}"
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

sheety_url = os.getenv("SHEETY_ENDPOINT")

nutri_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json",
}

params = {
    "query": input("What exercises did you do?") # only param required
}

response = requests.post(url=NATTY_FULL_ENDPOINT, headers=nutri_headers, json=params)
resp_json = response.json()["exercises"]

for index, item in enumerate(resp_json):

    payload = {
        "workout": {
            "date": dt.datetime.now().strftime("%x"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": resp_json[index]["name"],
            "duration": resp_json[index]["duration_min"],
            "calories": resp_json[index]["nf_calories"],
        }
    }
    sheety_headers = {
        "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
    }

    sheety_r = requests.post(
        sheety_url, 
        json=payload, 
        headers=sheety_headers)
    
    print("sheety.text", sheety_r.text)
    print("json dumps", json.dumps(payload))



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

2. AI says: response.text gives you a string. You'd need to manually parse it with json.loads().
response.json() gives you a ready-to-use dict --> and easier access to keys and values.

3. I was using the correct logic. But on response.text instead of the .json().

4. Using json=payload automatically sets Content-Type: application/json for me.

"""



