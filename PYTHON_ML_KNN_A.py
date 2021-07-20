from sklearn.neighbors import KNeighborsClassifier

import requests
import pandas as pd 
import io

import numpy as np
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/devrescue/python/main/datasets/SPECTF.csv'

s = requests.get(url).content

df = pd.read_csv(io.StringIO(s.decode('utf-8')))

#some information about our dataset
print(df.info())

#count of classes in the dataset
print(len(df[df.OVERALL_DIAGNOSIS == 0])) #normal
print(len(df[df.OVERALL_DIAGNOSIS == 1])) #abnormal

#histogram of Normal vs Abnormal classes
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
diagnoses = ['NORMAL', 'ABNORMAL']
patients = [len(df[df.OVERALL_DIAGNOSIS == 0]),len(df[df.OVERALL_DIAGNOSIS == 1])]
ax.bar(diagnoses,patients)
plt.show()

#labels y
y = df['OVERALL_DIAGNOSIS'].values 

#training data X
X = df.drop('OVERALL_DIAGNOSIS', axis=1).values 

#our classifier
knn = KNeighborsClassifier(n_neighbors=7)

knn.fit(X,y)

# predict labels for training data X
y_pred = knn.predict(X)