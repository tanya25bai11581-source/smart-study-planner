import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# training data
data = pd.read_csv("data.csv")

X = data[["difficulty", "chapters", "days"]]
y = data["priority"]

model = DecisionTreeRegressor()
model.fit(X, y)

def predict_priority(difficulty, chapters, days):
    test = pd.DataFrame([[difficulty, chapters, days]],
                        columns=["difficulty", "chapters", "days"])
    return int(model.predict(test)[0])
