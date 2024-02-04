from app import app
from flask import render_template, redirect, request
import login, register

@app.route("/login", methods=["GET"])
def getLogin():
    if request.method == "GET":
       return render_template("login.html")
    
@app.route("/login", methods=["POST"])
def postLogin():
    username = request.form["username"]
    password = request.form["password"]

    if login.login(username, password):
        return redirect("/")

    return render_template("login.html", error="Invalid username or password")

@app.route("/register")
def getRegister():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def postRegister():
    username = request.form["username"]
    password = request.form["password"]
    passwordConfirmation = request.form["passwordConfirmation"]

    if password != passwordConfirmation:
        render_template("register.html", error="Passwords are not matching")
    
    if register.register(username, password):
        redirect("/")
    else:
        render_template("register.html", error="Username taken")