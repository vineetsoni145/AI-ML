import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("students (1).csv")

y = df["Marks (%)"]
X = df[["Sleep Hours"]]

sleep_model = LinearRegression()
sleep_model.fit(X, y)

print("Sleep Model:")
