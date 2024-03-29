from app import app
from flask import render_template, redirect, request, url_for
import login, register, group, thread, comment, likes

def renderThread(threadId, groupId):
    threadById = thread.getThreadById(threadId)
    threadComments = comment.getCommentsInThread(threadId)
    threadLikes = likes.getThreadLikes(threadId)

    return render_template("thread.html", thread=threadById, comments=threadComments, group=groupId, likes=threadLikes)

def redirectToThread(threadId, groupId):
    return redirect(url_for('getThread', groupId=groupId, threadId=threadId))



@app.route("/login", methods=["GET"])
def getLogin():
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

    if len(username) < 3:
        return render_template("register.html", error="Username too short. It must be at least 3 characters")
    
    if len(password) < 4:
        return render_template("register.html", error="Password too short. Must be at least 4 characters")


    if password != passwordConfirmation:
        return render_template("register.html", error="Passwords are not matching")
    
    if register.register(username, password):
        return render_template("login.html")
    else:
        return render_template("register.html", error="Username taken")

@app.route("/groups/new", methods=["POST"])
def postNewGroup():
    name = request.form["name"]
    description = request.form["description"]

    if len(name) < 3:
        return redirect("/groups")
    
    if len(description) < 3:
        return redirect("/groups")

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

@app.route("/groups/<int:id>", methods=["GET"])
def getGroup(id):
    groupById = group.getOneGroup(id)
    threads = thread.getThreadsInGroup(id)
    return render_template("group.html", group=groupById, threads=threads)

@app.route("/groups/<int:id>/threads", methods=["POST"])
def createThread(id):
    title = request.form["title"]
    content = request.form["content"]

    if thread.createThread(id, content, title):
        groupById = group.getOneGroup(id)
        threads = thread.getThreadsInGroup(id)
        return render_template("group.html", group=groupById, threads=threads)
    
    return redirect("/")

@app.route("/groups/<int:groupId>/threads/<int:threadId>/like", methods=["POST"])
def likeThread(groupId, threadId):
    userId = login.getUserId()
    if likes.hasUserLikedThread(userId, threadId):
        return redirectToThread(threadId, groupId)
    
    if likes.addLikeToThread(threadId):
        return redirectToThread(threadId, groupId)
        
    return redirect("/")

@app.route("/groups/<int:groupId>/threads/<int:threadId>")
def getThread(groupId, threadId):
    return renderThread(threadId, groupId)

@app.route("/groups/<int:groupId>/threads/<int:threadId>/comments", methods=["POST"])
def createCommentForThread(groupId, threadId):
    content = request.form["comment"]
    if comment.createComment(threadId, content):
        return redirectToThread(threadId, groupId)
      
    return redirect("/")
        