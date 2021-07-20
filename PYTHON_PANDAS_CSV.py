# Import packages
import requests
import pandas as pd #pip install pandas
import io

url = 'https://raw.githubusercontent.com/devrescue/python/main/datasets/boxoffice.csv'

s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

print(df.info())
print(df.head())
print(df.describe())
print(df["lifetime_gross"].describe().apply(lambda x: format(x, 'f')))
print(df.tail())

print(df.iloc[[0,16541]])
print(df.iloc[:5,[1,3,4]])
df[df["lifetime_gross"] > 500000000]