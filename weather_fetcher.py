# This simple weather fetcher will show you the weather in any city you type.
# https://openweathermap.org/api
# Using the link above, you can go to the weather API,
# create an account and get your own API key to run this code using your terminal.

import requests

API_KEY = "enter your API key here"
BASE_URL = "use the correct URL to obtain the info and enter it here"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error has occurred.")
