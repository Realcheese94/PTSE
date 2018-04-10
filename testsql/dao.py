from django.db import connection
from .models import SUser

#로그인을 위한 모든 아이디 비밀번호 확인 검사
def bringalluser():
    cursor = connection.cursor()
    query_string = "select * from testsql_suser"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts=[]
    for row in rows:
        dic ={'no':row[0],'id':row[1],'pw':row[2],'name':row[3],'tel':row[4]}
        posts.append(dic)
    return posts

def bringalluserid():
    cursor = connection.cursor()
    query_string = "select SuserId from testsql_suser"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts=[]
    for row in rows:
        posts.append(row[0])
    return posts

    
    



        
    