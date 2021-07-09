import requests
import json

#make sure you get you ALPHA VANTAGE API Key @ https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&datatype=json&outputsize=compact&apikey=DEMOKEY'
r = requests.get(url)
data = r.json()

print(json.dumps(data, indent=1))