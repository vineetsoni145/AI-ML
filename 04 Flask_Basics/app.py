from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    age = 0 
    # color = ""

    if request.method == "POST":
        Your_name = request.form.get("username")

        birth_year = int(request.form.get("br"))
        current_year = 2026
        age = current_year - birth_year
        print(age)


    return render_template("index.html", age=age )

if __name__ == "__main__":
    app.run(debug=True)