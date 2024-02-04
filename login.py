from db import db
from werkzeug.security import check_password_hash
from flask import session
from sqlalchemy.sql import text

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if not user:
        return False

    if check_password_hash(user.password, password):
        session["user_id"] = user.id
        return True
    
    return False

def logout():
    del session["user_id"]
