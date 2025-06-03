import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "topsecret"

latitude = 52.520008
longitude = 13.404954

weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key
}

# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}")

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
for item in data["list"]:
    print(item["weather"][0]["id"], ":", item["weather"][0]["description"])

