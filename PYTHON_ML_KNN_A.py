from sklearn.neighbors import KNeighborsClassifier
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

spectf = os.path.join("datasets","SPECTF.csv")

df = pd.read_csv(spectf)

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






