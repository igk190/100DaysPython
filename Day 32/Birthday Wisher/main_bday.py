##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv ✔️

# 2. Check if today matches a birthday in the birthdays.csv ✔️

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

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

if len(bday_persons) != 0:
    print("Omg someone has their bday!")
else:
    print("No parties today.")
# bday_person = bdays[(bdays["month"] == now.month) & (bdays["date"] == now.date)]
# bday_person = bdays[bdays['month'] == now.month]

print("---2", bday_persons)






# now = dt.datetime.now()
# print(now.year)


""" Learnings
1. read_csv() param chunksize lets you read the data in smaller chunks, each iteration gives you a chunk.
Useful when processing data in batches, or when dataset is too large. 

2. Refer to this Stackoverflow article: 
https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values

3. 10 Ways to filter a pandas dataframe: https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html
"""


