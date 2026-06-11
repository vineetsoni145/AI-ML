from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

df = pd.read_csv("cancer patient data sets.csv")

df.drop("Patient Id", axis=1, inplace=True)
df["Level"] = df["Level"].map({"Low": 0,"Medium": 1,"High": 2})

X = df.drop("Level", axis=1)
y = df["Level"]

model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X, y)

print("Model Trained Successfully")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():

    values = [[
        int(request.form["age"]),
        int(request.form["gender"]),
        int(request.form["air_pollution"]),
        int(request.form["alcohol_use"]),
        int(request.form["dust_allergy"]),
        int(request.form["occupational_hazards"]),
        int(request.form["genetic_risk"]),
        int(request.form["chronic_lung_disease"]),
        int(request.form["balanced_diet"]),
        int(request.form["obesity"]),
        int(request.form["smoking"]),
        int(request.form["passive_smoker"]),
        int(request.form["chest_pain"]),
        int(request.form["coughing_of_blood"]),
        int(request.form["fatigue"]),
        int(request.form["weight_loss"]),
        int(request.form["shortness_of_breath"]),
        int(request.form["wheezing"]),
        int(request.form["swallowing_difficulty"]),
        int(request.form["clubbing_of_finger_nails"]),
        int(request.form["frequent_cold"]),
        int(request.form["dry_cough"]),
        int(request.form["snoring"])
    ]]

    prediction = model.predict(values)[0]

    if prediction == 0:
        risk = "LOW RISK"
        advice = "Based on the provided information, the patient appears to have a low risk of lung cancer."

    elif prediction == 1:
        risk = "MEDIUM RISK"
        advice = "Some risk factors associated with lung cancer were detected. Please consult a healthcare professional."

    else:
        risk = "HIGH RISK"
        advice = "Multiple high-risk factors were detected. Please consult a doctor immediately."

    return render_template("index.html",risk=risk,advice=advice)


if __name__ == "__main__":
    app.run(debug=True)