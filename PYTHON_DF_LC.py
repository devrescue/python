import pandas as pd
from numerize import numerize

data = {'TOP10': ['United States','China','Japan','Germany','India','United Kingdom','France','Italy','Brazil','Canada']}
df = pd.DataFrame(data)

print(df)

upperCaseNames = [x.upper() for x in df["TOP10"]]
print(upperCaseNames)

forwardAndReverse = [(x.upper(),x.upper()[::-1]) for x in df["TOP10"]]
print(forwardAndReverse)

data = {'Country Name': ['United States','China','Japan','Germany','India','United Kingdom','France','Italy','Brazil','Canada'],
        'GDP 2021 Est. Trillions':[22675271000000,16642318000000,5378136000000,4319286000000,3124650000000,3049704000000,2938271000000,2106287000000,1883487000000,1806707000000]}
df = pd.DataFrame(data, index = [1,2,3,4,5,6,7,8,9,10])
print(df)

df["Country Name"] = [x.upper() for x in df["Country Name"]]
print(df)

df["GDP 2021 Est. Trillions"] = [ numerize.numerize(x) for x in df["GDP 2021 Est. Trillions"]]
print(df)