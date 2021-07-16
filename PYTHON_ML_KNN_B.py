# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import os
import pandas as pd

spectf = os.path.join("datasets","SPECTF.csv")

df = pd.read_csv(spectf)

#labels y
y = df['OVERALL_DIAGNOSIS'].values 

#features X
X = df.drop('OVERALL_DIAGNOSIS', axis=1).values 

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42, stratify=y)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train,y_train)

# Print the accuracy
print(knn.score(X_test, y_test))