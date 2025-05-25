import datetime as dt 
from random import randint
import smtplib

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday() # starts counting from zero

# date_of_birth = dt.datetime(year=1995, month=12, day=15,hour=4)

all_quotes = [] # will have 102 lines

with open("quotes.txt") as quotes:
    for line in quotes:
        all_quotes.append(line)

my_email = "xyz@gmail.com"
password = "abcd1234()"

if day == 6:
    print("wow it's sunday")
    with smtplib.SMTP("smtp.gmail.com") as connection: 
        connection.starttls() # ensures encryption
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="abc@hotmail.com", 
            msg=f"Subject:Sunday Motivation\n\n{all_quotes[randint(0, len(all_quotes)-1)]}"
            # msg=f"Subject:Sunday Motivation\n\n{all_quotes[0]}"
            )




""" Learnings
1. Instead of adding lines to a new list, with open("quotes.txt") as file: 
    all_qutotes = file.readlines()
    quote = random.choice(all_quotes)

2. Add content in msg with 2 newlines \n\n.
"""





