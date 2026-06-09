from flask import Flask, render_template, request

app = Flask(__name__)

dataset = {
    "TV": 10,
    "Mobile": 10,
    "Fridge": 45
}


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        choice = request.form["choice"]
        product = request.form["product"]
        quantity = request.form["quantity"]

        if quantity:
            quantity = int(quantity)

        if choice == "add":

            username = request.form["username"]
            password = request.form["password"]

            if username == "admin" and password == "admin123":

                dataset[product] = quantity
                message = "Product Added Successfully"

            else:
                message = "Wrong Username or Password"

        elif choice == "purchase":

            if product in dataset:

                dataset[product] -= quantity
                message = f"{quantity} {product} purchased successfully"

            else:
                message = "Product Not Found"

        elif choice == "return":

            if product in dataset:

                dataset[product] += quantity
                message = f"{quantity} {product} returned successfully"

            else:
                message = "Product Not Found"

        elif choice == "update":

            if product in dataset:

                dataset[product] += quantity
                message = f"{product} stock updated"

            else:
                message = "Product Not Found"

        elif choice == "check":

            message = "Current Stock Displayed Below"

    return render_template(
        "index.html",
        data=dataset,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)