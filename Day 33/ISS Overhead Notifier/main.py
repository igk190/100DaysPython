import requests
from datetime import datetime
import smtplib
import time 

MY_LAT = 52.520008
MY_LNG = 13.404954
MY_EMAIL = "abc@gmail.com" 
MY_PASSWORD = "blabal"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sun_data = response.json()

sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

def check_iss():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    time_now = datetime.now()

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LNG - 5) <= iss_longitude <= (MY_LNG+ 5):
        if time_now.hour >= sunset or time_now.hour <= sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection: 
                connection.starttls() # ensures encryption
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL, 
                    to_addrs=MY_EMAIL, 
                    msg=f"Subject:Look up! \n\nOr you'll miss it"
                    )

while True:
    check_iss()
    time.sleep(60)

#If the ISS is close to my current position
#Your position is within +5 or -5 degrees of the ISS position.
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


