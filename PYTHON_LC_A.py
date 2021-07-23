listA = [1,2,3,4]
listB = [5,6,7,8]

listC = [ A * B for A,B in zip(listA,listB)]
print(listC)

import pandas as pd

data = {'Country Name': ['Sundar','Jamal','Mark','Jenny','Bob'],
        'Year 1 Income':[250555,100300,45000,66000,1400000],
        'Year 2 Income':[250000,110300,45000,0,2400000]}

df = pd.DataFrame(data)

listD = [ B - A  for A,B in zip(df["Year 1 Income"],df["Year 2 Income"])]

print(listD)


listE = [1,2,3,4]
listF = [5,6,7,8]
listG = [9,10,11,12]

listH = [ E+F+G for E,F,G in zip(listE,listF,listG)]

print(listH)


listI = [1,2,3,4]
listJ = [5,6,7,8]

listK = [[I, J] for I in listI 
                for J in listJ]

print(listK)

listL=[]
x=[]

for I in listI:
    for J in listJ:
        listL.append([I,J])

print(listL)