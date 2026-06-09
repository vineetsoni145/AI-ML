#created a dashboard with multiple button like total sum, avg, etc but it will take user input 

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

df = None

@app.route("/", methods=["GET", "POST"])
def index():

    global df

    rows = 0
    cols = 0
    columns = []
    result = None
    error = None

    if request.method == "POST":

        if "csv_file" in request.files:

            file = request.files["csv_file"]

            if file.filename == "":
                error = "Select CSV File"

            elif file.filename.endswith(".csv"):

                df = pd.read_csv(file)

            else:
                error = "Upload Only CSV File"

        
        elif "calculation" in request.form:

            column = request.form["column"]

            if column == "":
                error = "Enter Column Name"

            elif column not in df.columns:
                error = "Column Not Found"

            else:

                if request.form["calculation"] == "sum":
                    result = df[column].sum()

                elif request.form["calculation"] == "avg":
                    result = df[column].mean()


    if df is not None:

        rows = df.shape[0]
        cols = df.shape[1]
        columns = df.columns.tolist()

    return render_template("user.html",rows=rows,cols=cols,columns=columns,result=result,error=error)

if __name__ == "__main__":
    app.run(debug=True)