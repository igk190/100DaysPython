import requests
import os
from datetime import datetime as dt, timedelta
from itertools import islice
import json

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query" # https://www.alphavantage.co/documentation/#daily
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
AV_API_KEY = os.getenv("AV_API_KEY")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "datatype": "json",
    "apikey": AV_API_KEY
}

"""response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
print(response.status_code, "\n")
stock_data = response.json()""" # reached API request limit of 25/day

stock_data = {'2025-06-06': {'1. open': '267.9900', '2. high': '270.1700', '3. low': '267.5300', '4. close': '268.8700', '5. volume': '2495543'}, '2025-06-05': {'1. open': '265.2000', '2. high': '267.5100', '3. low': '265.1000', '4. close': '266.8600', '5. volume': '2659478'}}

yesterday = (dt.now() - timedelta(1)).strftime('%Y-%m-%d')
day_before_yesterday = (dt.now() - timedelta(2)).strftime('%Y-%m-%d')

stock_yesterday = stock_data[yesterday]["4. close"]
stock_yesterday = int(stock_yesterday.replace(".", ""))
stock_day_before_yesterday = stock_data[day_before_yesterday]["4. close"]
stock_day_before_yesterday = int(stock_day_before_yesterday.replace(".", ""))

price_diff = ((stock_day_before_yesterday - stock_yesterday) / stock_yesterday) * 100

if abs(price_diff) > 5:
    print("Get news")

# print(stock_data["Time Series (Daily)"]["2025-06-06"]["4. close"])
# closing_prices = [value for (key, value) in stock_data["Time Series (Daily)"]]
# closing_prices = dict(islice(stock_data["Time Series (Daily)"].items(), 2))


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related 
# to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 
# 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation



## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description 
# using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


""" Learnings

1. os.getenv() is shorthand for os.environ.get(), never commit sensitive data to public repo.

2. datetime module has a "timedelta" object that lets you create spans of time. It gives you
the duration of one day and you can subtract it from datetime objects: 
yesterday = datetime.now() - timedelta(1)
https://stackoverflow.com/questions/30483977/python-get-yesterdays-date-as-a-string-in-yyyy-mm-dd-format

3. Remove sign in front of number with abs(): https://www.w3schools.com/python/ref_func_abs.asp

4. Quite challenging to access a dict key, based on a daily changing date. Implemented
a workaround with datetime.now() minus timedelta(1 or 2), formatting it the same way
as it's displayed in the API response, then inserting that as the key.
"""

