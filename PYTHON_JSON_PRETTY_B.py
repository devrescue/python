import requests
import json

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
r = requests.get(url)
data = r.json()

pretty_json = json.dumps(data, indent=1)

from pygments import highlight, lexers, formatters
color_json = highlight(str(pretty_json), lexers.JsonLexer(), formatters.TerminalFormatter())

print(color_json)

