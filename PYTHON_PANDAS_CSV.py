# Import packages
import os
import pandas as pd #pip install pandas

boxoffice = os.path.join("boxoffice.csv")

df = pd.read_csv(boxoffice)

print(df.info())
print(df.head())
print(df.describe())
print(df["lifetime_gross"].describe().apply(lambda x: format(x, 'f')))
print(df.tail())