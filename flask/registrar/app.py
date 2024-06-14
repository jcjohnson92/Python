from flask import Flask, render_template, request, redirect

app = Flask(__name__)

REGISTRANTS = {}
SPORTS = ["Soccer","Basketball","Ultimate Frisbee"]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")

    if not name:
        return render_template("error.html", message="Missing name")
    
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing Sport")
    if not SPORTS:
        return render_template("error.html", message="Invalid SPORT")

    # remeber registrars
    REGISTRANTS[name]=sport
    
    for x,y in REGISTRANTS.items():
        print(x,y)

    return redirect("/registrants")

    
    # return render_template("success.html", name=name, sports=SPORTS)

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)

    
