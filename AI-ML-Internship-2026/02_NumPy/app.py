import csv
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        file = request.files["csv_file"]

        if file.filename == "":
            return render_template("index.html",error="select a CSV file")

        if not file.filename.endswith(".csv"):
            return render_template("index.html",error="Upload Only CSV files")

        lines = file.stream.read().decode("utf-8").splitlines()
        reader = list(csv.reader(lines))

        rows = len(reader)

        if rows > 0:
            cols = len(reader[0])
        else:
            cols = 0

        return render_template("index.html",rows=rows,cols=cols,filename=file.filename)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)