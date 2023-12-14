import pandas as pd
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo

ref = ["No", "Yes"]

# fetch dataset
spambase = fetch_ucirepo(id=94)

# data (as pandas dataframes)
x = spambase.data.features.values
y = spambase.data.targets.values

#Standardizes the x values
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

#Splits the data into a training and testing set
x_train, x_test, y_train, y_test = train_test_split(x, y)

#Creates the logisitic regression model
model = linear_model.LogisticRegression().fit(x_train, y_train)

#Prints the accuracy and predictions of the model
print("Testing Results:")
print("")
print(y_test)
for index in range(len(x_test)):
    x = x_test[index]
    x = x.reshape(-1, 57)
    y_pred = model.predict(x)[0]
    actual = y_test[index][0]

    print("Predicted: " + ref[y_pred] + "; Actual: " + ref[actual])
    print("")

print("*************")
print("Accuracy:", model.score(x_test, y_test))
