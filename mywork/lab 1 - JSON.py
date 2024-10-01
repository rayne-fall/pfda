# lab 1 - JSON
# author: Sylvia Chapman Kent
# read in JSON from a URL , print the data and output the current price of Bitcoin in Euros

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data['bpi']['EUR']['rate_float'])