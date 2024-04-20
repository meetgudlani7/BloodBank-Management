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

@app.route('/donor')
def donorpage():
    return render_template("donor.html")

@app.route('/bloodbankregister')
def bloodbankpage():
    return render_template("bloodbankregister.html")

@app.route('/hospregister')
def hospitalpage():
    return render_template("hospregister.html")

@app.route('/request',methods=["POST","GET"])
def requestpage():
    if request.method == "POST":
        name = request.form["name"]
        bloodgroup = request.form["bloodgroup"]
        hospid = request.form["hospid"]
        bankid = request.form["bankid"]
        addPatient(name, bloodgroup, hospid, bankid)
        return redirect(url_for("mainpage"))
    return render_template("request.html",hosps = getHosp(), banks = getBBank())

@app.route('/howtodonate')
def howtodonatepage():
    return render_template("howtodonate.html")

@app.route('/about')
def aboutpage():
    return render_template("about.html")

@app.route('/contact')
def contactpage():
    return render_template("contact.html")

@app.route('/benefits')
def benefitspage():
    return render_template("benefits.html")

@app.route('/donordet')
def donordet():
    return render_template("donordet.html")

@app.route('/donorreg',methods=["POST","GET"])
def donorregpage():
    if request.method == "POST":
        name = request.form["name"]
        gender = request.form["gender"]
        address = request.form["address"]
        pno = request.form["phone_number"]
        weight = request.form["weight"]
        dob = request.form["dob"]
        docid = request.form["docid"]
        adddonor(name,gender,address,pno,weight,dob,docid)
        return redirect(url_for("donorpage"))
    return render_template("donorreg.html",docs = getDocs())

@app.route('/bloodbankregform',methods=["POST","GET"])
def bloodbankregformpage():
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        addBloodBank(name,address)
        return redirect(url_for("bloodbankpage"))
    return render_template("bloodbankregform.html")

@app.route('/hospregform',methods=["POST","GET"])
def hospregformpage():
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        mode = request.form["mode"]
        addhospital(name,address,mode)
        return redirect(url_for("hospitalpage"))
    return render_template("hospregform.html")


if __name__ == '__main__':
    app.run(debug=True)