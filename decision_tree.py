import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import features_extraction

def getResult(url):
    data = pd.read_csv("detect_phishing_website.csv")
    # Removing Unnecessary columns
    data.drop(["id"], axis=1, inplace=True)
    # Removing Null values
    data = data.dropna()
    # Define X && Y
    y = data.Result
    x = data.drop('Result', axis=1)
    # splitting the data into train data and test data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    # Creating the model and fitting the data into the model
    dt = DecisionTreeClassifier(random_state=0)
    dt.fit(x_train, y_train)
    # Predicting the result for test data
    y_predict = dt.predict(x_test)
    score = dt.score(x_test, y_test)
    print(100 * score)
    X_new = []

    X_input = url
    X_new = features_extraction.generate_data_set(X_input)

    X_new = np.array(X_new).reshape(1, -1)
    # print(X_new)

    try:
        prediction = dt.predict(X_new)
        if prediction ==-1:
            return "Phishing Url"
        else:
            return "Legitimate Url"
    except:
        return "Phishing Url"

# getResult("http://www.abchnia.com.cn/")




