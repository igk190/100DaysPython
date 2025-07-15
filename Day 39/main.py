#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import requests 
import json
from pprint import pprint

SHEETY_FLIGHTDEALS_ENDPOINT = os.getenv("SHEETY_FLIGHTDEALS_ENDPOINT")
SHEETY_FLIGHTDEALS_BEARER_TOKEN = os.getenv("SHEETY_FLIGHTDEALS_BEARER_TOKEN")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_FLIGHTDEALS_BEARER_TOKEN}"
}

# sheety_r = requests.get(SHEETY_FLIGHTDEALS_ENDPOINT, headers=sheety_headers)
# sheet_data = sheety_r.json()
# pprint(sheet_data["prices"]) 

sheet_data = [
    {'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
    {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
    {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
    {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
    {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
    {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
    {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
    {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
    {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378}
    ]
pprint(sheet_data)

field_key = ""

for index, el in enumerate(sheet_data):
    if el["iataCode"] == "":
        print(f"{index} Empty!")
        el["iataCode"] = "TESTING"
    else:
        print(el["iataCode"])

for item in sheet_data:
    print(item["iataCode"])

pprint(sheet_data)






""" Learnings

1. Uh oh. After one month of learning Java at school, I seem to have forgotten most of my Python. 
Shows the importance of maintaining momentum. Let's recreate some.

2. Recapping: give requests arguments as a dict of strings, using the params kwarg.
example: payload = {'key1': 'value1', 'key2':'value2'}
r = requests.get('Someendpoint/', params=payload)
print(r.url) --> You'll see it gets correctly encoded.

3. Recapping 2.0: 

r = requests.get("someurl")
r.json() to use the built-in JSON decoder

To check if a request is successful:
r.raise_for_status()

To add headers, pass in a dict to the headers param (see requests documentation)
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

To send form-encoded data: pass a dict to the 'data' arg.


4. Object ID is just the row number in Sheety.

"""