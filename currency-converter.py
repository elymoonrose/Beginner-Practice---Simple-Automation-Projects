# This is a simple currency converter that allows you to see the monetary value of the base currency you choose.
# In this case only COP, USD, CAD and EUR are available, but you can add more.
# https://app.currencyapi.com/
# Using the link above, you can go to the currency API,
# create an account and get your own API key to run this code using your terminal.

import requests

API_KEY = "enter your API key here"
BASE_URL = f"use the correct URL to obtain the info and enter it here{API_KEY}"
CURRENCIES = ["COP", "USD", "CAD", "EUR"]


def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid currency.")
        return None


while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
