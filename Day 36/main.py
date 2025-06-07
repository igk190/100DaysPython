import requests
import os
from datetime import datetime as dt, timedelta
import json
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query" # https://www.alphavantage.co/documentation/#daily
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
AV_API_KEY = os.getenv("AV_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_ACC_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN) # proxy needed?

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "datatype": "json",
    "apikey": AV_API_KEY
}

# Get data from API call
"""response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
print(response.status_code, "\n")
stock_data = response.json()""" # reached API request limit of 25/day ["Time Series (Daily)"]

stock_data = {'2025-06-06': {'1. open': '267.9900', '2. high': '270.1700', '3. low': '267.5300', '4. close': '268.8700', '5. volume': '2495543'}, '2025-06-05': {'1. open': '265.2000', '2. high': '267.5100', '3. low': '265.1000', '4. close': '266.8600', '5. volume': '2659478'}}

# Get yesterday's and day before yesterday's date, convert to string
# yesterday = (dt.now() - timedelta(1)).strftime('%Y-%m-%d')
# day_before_yesterday = (dt.now() - timedelta(2)).strftime('%Y-%m-%d')

yesterday = (dt.now() - timedelta(2)).strftime('%Y-%m-%d')              # testing
day_before_yesterday = (dt.now() - timedelta(3)).strftime('%Y-%m-%d')   # testing

# Use date strings to access objects in stock_data
stock_yesterday = float(stock_data[yesterday]["4. close"])
stock_day_before_yesterday = float(stock_data[day_before_yesterday]["4. close"])

price_diff = ((stock_day_before_yesterday - stock_yesterday) / stock_yesterday) * 100

# Get 3 news articles from COMPANY_NAME via newsapi.org
testnum = 6
# if abs(price_diff) > 5:
if testnum > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    first_3_articles = news_data["articles"][:3]
    print(first_3_articles)

# first_3_articles = [{'source': {'id': None, 'name': 'Techmeme.com'}, 'author': None, 'title': "The Greater Memphis Chamber says xAI is using Tesla's 150MW Megapack batteries to shore up its Colossus supercomputer; xAI spent ~$230M on them in 2024 and 2025 (Dana Hull/Bloomberg)", 'description': "Dana Hull / Bloomberg:\nThe Greater Memphis Chamber says xAI is using Tesla's 150MW Megapack batteries to shore up its Colossus supercomputer; xAI spent ~$230M on them in 2024 and 2025\xa0 —\xa0 Elon Musk's xAI is using Tesla Inc.'s Megapack batteries to shore up it…", 'url': 'https://www.techmeme.com/250508/p19', 'urlToImage': 'https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iJpNz6.xNhyo/v1/1200x800.jpg', 'publishedAt': '2025-05-08T10:10:01Z', 'content': 'About This Page\r\nThis is a Techmeme archive page.\r\nIt shows how the site appeared at 6:10\xa0AM\xa0ET, May\xa08,\xa02025.\r\nThe most current version of the site as always is available at our home page.\r\nTo view a… [+65 chars]'}, {'source': {'id': None, 'name': 'Habr.com'}, 'author': 'nikolz', 'title': '[Перевод] Как Искусственный Интеллект уже изменил мою работу', 'description': 'Работники из разных отраслей промышленности рассказывают о том, как они адаптируются. Интернет полон мыслей о том, как искусственный интеллект\xa0изменит работу. Все возможные прогнозы уже сделаны: ИИ\xa0заберёт все наши рабочие места. Или, может быть, только низко…', 'url': 'https://habr.com/ru/articles/909686/#post-content-body', 'urlToImage': 'https://habr.com/share/publication/909686/b1f9e27510140eade0e7eb2817ca177a/', 'publishedAt': '2025-05-15T10:27:34Z', 'content': ', .\r\n , \xa0. : \xa0. , , . , , . , , , ,\xa0. (-.)\r\n , , . \xa0Bloomberg Businessweek\xa0 , . , , , ,\xa0; Uber, Waymo,\xa0; , , \xa0\xa0 .\r\n, \xa0? , .\r\n .\r\nSamantha Lackney\r\n, \r\n , - , , , , . , , , , , , . , , « » . , , .\r\n ,… [+1001 chars]'}, {'source': {'id': None, 'name': 'Forbes'}, 'author': 'Trefis Team, Contributor, \n Trefis Team, Contributor\n https://www.forbes.com/sites/greatspeculations/people/trefis/', 'title': 'What Are The Odds Of Tesla Stock Declining To $150?', 'description': 'Tesla Inc dropped 14% in a single day yesterday, representing one of its most significant one-day falls in the past few years.', 'url': 'https://www.forbes.com/sites/greatspeculations/2025/06/06/what-are-the-odds-of-tesla-stock-declining-to-150/', 'urlToImage': 'https://imageio.forbes.com/specials-images/imageserve/64bdfc53faa55c0f439a6bb7/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds', 'publishedAt': '2025-06-06T12:00:19Z', 'content': 'Tesla Motors logo. (Photo by Smith Collection/Gado/Getty Images)\r\nGetty Images\r\nTesla Inc. (NASDAQ: TSLA)\r\n dropped 14% in a single day yesterday, representing one of its most significant one-day fal… [+5533 chars]'}]
    for index, item in enumerate(first_3_articles):
        message = client.messages.create(
        body=f'{item["title"]}\n{item["description"]}',
        from_=os.environ.get("TWILIO_FROM_NUM"),
        to=os.environ.get("WA_NUM"))
        print(message.status)
        
        # print(index, item["title"])
        # print(index, item["description"])
    
    # proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    # client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)



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

4a. Quite challenging to access a dict key, based on a daily changing date. Implemented
a workaround with datetime.now() minus timedelta(1 or 2), formatting it the same way
as it's displayed in the API response, then inserting that as the key.

4b. List comprehension on dict would've worked !
test_list = [value for (key, value) in stock_data.items()] 
- go through items in Time Series (Daily)
- each object for each day, add this in its entirety to the list
- access the dict with yesterday = test_list[0]
- and the key-value pairs inside the object by the key name test_list[0]["4. close"]
Done.

5. Ups, instead of removing the dot with replace() and then wrapping the numbers in
int(), I could've converted the strings to float().

6. Use enumerate to lists with objects inside.

7. If slice from start, you don't need 0. Just write ":3."

8. Run the script at a time in your time zone when stock markets have closed!

Notes:

- For list comprehension revision, go to Day 26.
- Digging deeper: stock_data["Time Series (Daily)"]["2025-06-06"]["4. close"])
- Explore islice further:
    - from itertools import islice \n closing_prices = dict(islice(stock_data["Time Series (Daily)"].items(), 2))

"""

