from flask import Flask, render_template, request

app = Flask(__name__)

health = 200
kills = 0
ammo = 0
heals = 0
zone = 8


def reset_game():

    global health
    global kills
    global ammo
    global heals
    global zone
    health = 200
    kills = 0
    ammo = 0
    heals = 0
    zone = 8


@app.route("/", methods=["GET", "POST"])
def home():

    global health
    global kills
    global ammo
    global heals
    global zone

    message = ""

    if request.method == "POST":
        choice = request.form["choice"].lower()

        if choice == "new":
            reset_game()

        elif health > 0 and zone > 0:

            if choice == "kill":
                health -= 30
                kills += 1

            elif choice == "loot":
                ammo += 30
                heals += 1

            elif choice == "hide":
                health -= 10
            zone -= 1

        if health <= 0:
            message = "💀 GAME OVER"

        elif zone <= 0:
            message = "🏆 WINNER WINNER CHICKEN DINNER"

    return render_template(
        "index.html",
        health=health,
        kills=kills,
        ammo=ammo,
        heals=heals,
        zone=zone,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)