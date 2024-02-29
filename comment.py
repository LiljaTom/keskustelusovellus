from db import db
from sqlalchemy.sql import text
import login

def createComment(threadId, content):
    userId = login.getUserId()

    if userId == 0:
        return False
    
    try:
        sql = text("INSERT INTO comments (content, thread_id, user_id) VALUES (:content, :thread_id, :user_id)")
        db.session.execute(sql, {"content":content, "thread_id":threadId ,"user_id":userId})
        db.session.commit()

        return True
    except:
        return False
    
def getCommentsInThread(threadId):
    sql = text("SELECT content from comments WHERE thread_id=:thread_id")
    result = db.session.execute(sql, {"thread_id": threadId})

    return result.fetchall()