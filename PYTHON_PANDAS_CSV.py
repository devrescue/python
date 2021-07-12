# Import packages
import os
import pandas as pd #pip install pandas

boxoffice = os.path.join("datasets","boxoffice.csv")

df = pd.read_csv(boxoffice)

print(df.info())
print(df.head())
print(df.describe())
print(df["lifetime_gross"].describe().apply(lambda x: format(x, 'f')))
print(df.tail())

print(df.iloc[[0,16541]])
print(df.iloc[:5,[1,3,4]])
df[df["lifetime_gross"] > 500000000]