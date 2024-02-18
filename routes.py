from app import app
from flask import render_template, redirect, request
import login, register, group

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

@app.route("/logout")
def postLogout():
    login.logout()
    return redirect("/")

@app.route("/register")
def getRegister():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def postRegister():
    username = request.form["username"]
    password = request.form["password"]
    passwordConfirmation = request.form["passwordConfirmation"]


    if password != passwordConfirmation:
        return render_template("register.html", error="Passwords are not matching")
    
    if register.register(username, password):
        return redirect("/")
    else:
        return render_template("register.html", error="Username taken")

@app.route("/groups/new", methods=["POST"])
def postNewGroup():
    name = request.form["name"]
    description = request.form["description"]

    if group.createGroup(name, description):
        return redirect("/groups")
    
    return render_template("newGroup.html")

@app.route("/groups/new", methods=["GET"])
def getGroupFrom():
    return render_template("newGroup.html")

@app.route("/groups", methods=["GET"])
def getGroups():
    groupList = group.getGroups()
    return render_template("groups.html", groups=groupList)

@app.route("/groups/<int:id>")
def getGroup(id):
    groupById = group.getOneGroup(id)
    return render_template("group.html", group=groupById)