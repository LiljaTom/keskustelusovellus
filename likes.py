from db import db
from sqlalchemy.sql import text
import login

def addLikeToThread(threadId):
    userId = login.getUserId()

    if userId == 0:
        return False
    
    try:
        sql = text("INSERT INTO threadlikes (thread_id, user_id) VALUES (:thread_id, :user_id)")
        db.session.execute(sql, {"thread_id":threadId, "user_id":userId})
        db.session.commit()
        return True
    except:
        return False