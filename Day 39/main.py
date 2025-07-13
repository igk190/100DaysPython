#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import requests

r = requests.get('someEndpoint') 

# TODOS 
"""sheety_flightdeals_url = os.getenv("SHEETY_FLIGHTDEALS_URL")
SHEETY_FLIGHTDEALS_BEARER_TOKEN = os.getenv("SHEETY_FLIGHTDEALS_BEARER_TOKEN")
sheety_headers = {
"Authorization": f"Bearer {SHEETY_FLIGHTDEALS_BEARER_TOKEN}
}
sheety_r = requests.get(sheety_flightdeals_url)
print(sheety_r.json())
"""






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

To add headers, pass in a dict to the headers param
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

To send form-encoded data: pass a dict to the 'data' arg.



"""