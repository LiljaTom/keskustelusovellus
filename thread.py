from db import db
from sqlalchemy.sql import text
import login

def createThread(groupId, content, title):
    userId = login.getUserId()

    if userId == 0:
        return False
    
    try: 
        sql = text("INSERT INTO threads (content, group_id, title, user_id) VALUES (:content, :group_id, :title, :user_id)")
        db.session.execute(sql, {"content":content, "group_id":groupId, "title":title, "user_id": userId})
        db.session.commit()
        return True
    except:
        return False
    
def getThreadsInGroup(groupId):
    sql = text("SELECT id, title, content FROM threads WHERE group_id=:group_id")
    result = db.session.execute(sql, {"group_id": groupId})

    return result.fetchall()

def getThreadById(threadId):
    sql = text("SELECT id, title, content from threads WHERE id=:threadId")
    result = db.session.execute(sql, {"threadId": threadId})
    return result.fetchone()
