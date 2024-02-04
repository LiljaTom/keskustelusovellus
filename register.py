from db import db
from werkzeug.security import generate_password_hash
from sqlalchemy.sql import text


def register(username, password):
    password_hash = generate_password_hash(password)

    try:
        sql = text("INSERT INTO users (username, password) VALUES (:username,:password)")
        db.session.execute(sql, {"username":username, "password": password_hash})
        db.session.commit()
        return True
    except:
        print("Username taken")
        print("Or some other error")
        return False