##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv ✔️

# 2. Check if today matches a birthday in the birthdays.csv ✔️

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv ✔️

# 4. Send the letter generated in step 3 to that person's email address. 

# 5. Check if df > 1 person has a bday, if so, send email to each.

import datetime as dt
import random
import smtplib
import pandas as pd

now = dt.datetime.now()
# print(now.day) # date of the month 

bdays = pd.read_csv("birthdays.csv", usecols=["name","email","month","date"]) # returns pandas df, defines cols to use

# newdf = bdays[(bdays.month == 5) & (bdays.date == 28)]
# newdf = bdays.query('month == 5 & date == 28')

bday_persons = bdays[(bdays['month'] == now.month) & (bdays['date'] == now.day)]
letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]

my_email = "abc@gmail.com"
password = "abc"

if len(bday_persons) != 0:
    print(len(bday_persons))
    print("Omg someone has their bday!")

    bday_letter = random.choice(letters)
    file_path = "letter_templates/" + bday_letter 

    with open(file_path, "r") as letter:
        search_text = "[NAME]"
        replace_text = bday_persons["name"].iloc[0]
        # print(replace_text) # Henkie
        
        contents = letter.read()
        contents = contents.replace(search_text, replace_text)
        # print(contents)

        # with smtplib.SMTP("smtp.gmail.com") as connection: 
        #     connection.starttls() # ensures encryption
        #     connection.login(user=my_email, password=password)
        #     connection.sendmail(
        #         from_addr=my_email, 
        #         to_addrs="abc@hotmail.com", 
        #         msg=f"Subject:Happy bday, {replace_text}\n\n{contents}"
        #         )
else:
    print("No parties today.")

# bday_person = bdays[(bdays["month"] == now.month) & (bdays["date"] == now.date)]
# bday_person = bdays[bdays['month'] == now.month]








# now = dt.datetime.now()
# print(now.year)


""" Learnings

1. read_csv() param chunksize lets you read the data in smaller chunks, each iteration gives you a chunk.
Useful when processing data in batches, or when dataset is too large. 

2. Refer to this Stackoverflow article: 
https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values

3. 10 Ways to filter a pandas dataframe: https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html

4. Search and replace text in a Python file: https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/ 

"""


