from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
import joblib


data = pd.read_csv("students (1).csv")


X = data[["play_time", "sleep_time", "study_hours"]]
y = data["result_percentage"]


model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)
score = r2_score(y, predictions)

print("STUDENT PERFORMANCE MODEL")
print(f"Intercept: {model.intercept_:.2f}")

for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")

print(f"R² Score = {score:.4f}")

joblib.dump(model, "student_result_model.pkl")

sample = pd.DataFrame({ "play_time": [3], "sleep_time": [8], "study_hours": [5]})
predicted_marks = model.predict(sample)

print(f"Predicted marks for "f"Play=3h, Sleep=8h, Study=5h: "f"{predicted_marks[0]:.2f}")
print("Model saved as student_result_model.pkl")
