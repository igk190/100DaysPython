import datetime as dt
import random
import smtplib
import pandas as pd

now = dt.datetime.now() # now.day for date of the month

bdays = pd.read_csv("birthdays.csv", usecols=["name","email","month","date"]) # returns pandas df, defines cols to use

bday_persons = bdays[(bdays['month'] == now.month) & (bdays['date'] == now.day)]
# newdf = bdays[(bdays.month == 5) & (bdays.date == 28)]        # alt 1
# newdf = bdays.query('month == 5 & date == 28')                # alt 2          
letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]

MY_EMAIL = "abc@gmail.com"
PASSWORD = "def"

if len(bday_persons) == 0:
    print("No parties today.😢")
elif len(bday_persons) >= 1:
    print("Get your gifts ready, put on your party hat🥳!\n")

    for index, row in bday_persons.iterrows():
        print(row["name"], "has their bday!\n")
        bday_letter = random.choice(letters)
        file_path = "letter_templates/" + bday_letter 
        
        with open(file_path, "r") as letter:
            contents = letter.read()
            contents = contents.replace("[NAME]", row["name"] )
            print(contents)
            with smtplib.SMTP("smtp.gmail.com") as connection: 
                connection.starttls() # ensures encryption
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL, 
                    to_addrs=row["email"], 
                    msg=f"Subject:Happy bday, {row['name']}\n\n{contents}"
                    )


""" Learnings

1. read_csv() param chunksize lets you read the data in smaller chunks, each iteration gives you a chunk.
Useful when processing data in batches, or when dataset is too large. 

2. Refer to this Stackoverflow article: 
https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values

3. 10 Ways to filter a pandas dataframe: https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html

4. Search and replace text in a Python file: https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/ 

5. Get a specific row in df: https://www.geeksforgeeks.org/get-a-specific-row-in-a-given-pandas-dataframe/

6. Loop through rows in a df: https://www.freecodecamp.org/news/how-to-iterate-over-rows-with-pandas-loop-through-a-dataframe/ 

7. Instead of picking a random letter from the letters dict, I could've just inserted random.randint for the letter number,
since only this value changes. 

After watching solution video:

1. today = datetime.now()
today_tuple = (today.month, today.day)
"""


