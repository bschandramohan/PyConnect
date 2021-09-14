import os
import requests
from dotenv import load_dotenv
import pandas

load_dotenv()  # This loads the .env file so that we can use os.getenv to get environment properties
stocklist_df = pandas.read_csv("stocks_watchlist.csv")
stock_tickers = stocklist_df["TICKER"]
# If required, we can iterate over all the watchlist items ; For now just take 1
symbol = stock_tickers[0]
# print(symbol)

AV_STOCK_API_KEY = os.getenv("av_stock_key")
AV_STOCKS_API_URL = "https://www.alphavantage.co/query"
PARAMS = f"?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={AV_STOCK_API_KEY}"


response = requests.get(AV_STOCKS_API_URL + PARAMS)
stock_perf_list = response.json()["Time Series (Daily)"]
response.close()

stock_trend = {}
handled_date = ""
for index, stock_data in enumerate(stock_perf_list):
    # print(index, stock_data)
    if index == 0:
        handled_date = stock_data
        continue

    daily_diff = float(stock_perf_list[stock_data]["4. close"]) - float(stock_perf_list[handled_date]["4. close"])
    if daily_diff > 0:
        trend_symbol = "📈"
    else:
        trend_symbol = "📉"

    stock_trend[stock_data] = f"Price (at close)={stock_perf_list[stock_data]['4. close']}. That is trending " \
                              f"{trend_symbol} by { str(abs(round(daily_diff, 2))) }"

    handled_date = stock_data

for date, trend in stock_trend.items():
    print(date, ":", trend)
