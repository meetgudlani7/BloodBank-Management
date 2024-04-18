from flask import flash,Flask,session,redirect,render_template,url_for,request
from check import *

app = Flask(__name__)
app.secret_key="Blood"

@app.route('/')
def index():
    return redirect(url_for("login"))

@app.route('/mainpage')
def mainpage():
    if "user" in session:
        return render_template("index.html")
    else:
        return redirect(url_for("index"))


@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["Username"]
        Password = request.form["Password"]
        if Login_check(username,Password):
            session["user"] = username
            return redirect(url_for("mainpage"))
        else:
            return redirect(url_for("index"))
    else:
        return render_template("login.html")
    
@app.route('/signup',methods=["POST","GET"])
def signup():
    if request.method == "POST":
        username = request.form["Username"]
        email = request.form["Email"]
        Password = request.form["Password"]
        if signup_check(username,email,Password):
            return redirect(url_for("index"))
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)