import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACC_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

latitude = 41.649693
longitude = -0.887712

weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": OWM_api_key,
    "cnt": 4
}

# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}")

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()

rain_is_coming = False

for item in weather_data["list"]:
    print(item["weather"][0]["id"], ":", item["weather"][0]["description"],
          item["dt_txt"])
    if int(item["weather"][0]["id"])  < 700:
        rain_is_coming = True

if rain_is_coming:
    proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

    client = Client(account_sid, twilio_auth_token, http_client=proxy_client)
    message = client.messages.create(
    body="It's gonna rain, gotta bring an umbrella!☂️",
    from_=os.environ.get("TWILIO_FROM_NUM"),
    to=os.environ.get("WA_NUM"))
    print(message.status)

    # message = client.messages.create(
    # from_="whatsapp:+geheim",
    # body="It's going to rain today. Remember to bring an umbrella",
    # to="whatsapp:+geheim"
    # )

    

""" Learnings

1. Instead of requests.get(url="..."), save the API endpoint as a string.
Save parameters separately in a dict. Then do requests.get(url=API_Endpoint, params=weather_params)
to keep things cleaner.

2. Access a list with the index, and a dict with the name of the key as a string.
"""

