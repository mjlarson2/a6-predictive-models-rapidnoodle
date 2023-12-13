import pandas as pd
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ucimlrepo import fetch_ucirepo

# fetch dataset
spambase = fetch_ucirepo(id=94)

# data (as pandas dataframes)
x = spambase.data.features
y = spambase.data.targets

#Standardizes the x values
scaler = StandardScaler().fit(x)
x = scaler.transform(x)

#Splits the data into a training and testing set
x_train, x_test, y_train, y_test = train_test_split(x, y)

#Creates the logisitic regression model
model = linear_model.LogisticRegression().fit(x_train, y_train)

#Prints the accuracy and predictions of the model
print("Accuracy:", model.score(x_test, y_test))
print("*************")
print("Testing Results:")
print("")
print(y_test)
for index in range(len(x_test)):
    x = x_test[index]
    x = x.reshape(-1, 57) # THIS IS THE PROBLEM
    y_pred = model.predict(x)[0]

    if y_pred == 0:
        y_pred = "1"
    else:
        y_pred = "0"
    
    actual = y_test[index]
    if actual == 0:
        actual = "1"
    else:
        actual = "0"
    print("Predicted Spam: " + y_pred + " Actual Spam: " + actual)
    print("")
