from db import db
from sqlalchemy.sql import text
import login


def createGroup(name, description):
    userId = login.getUserId()

    if userId == 0:
        return False
    
    sql = text("INSERT INTO groups (description, name, user_id) VALUES (:description, :name, :user_id)")
    db.session.execute(sql, {"description":description, "name": name, "user_id":userId})
    db.session.commit()
    
    return True

def getGroups():
    sql = text("SELECT description, name, id FROM groups")
    result = db.session.execute(sql)
    return result.fetchall()

