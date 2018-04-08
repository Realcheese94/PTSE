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
        dic ={'id':row[1],'pw':row[2]}
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

def insertnewuser(registuserinforms):
 
   ruserid =  registuserinforms["id"]
   ruserpw = registuserinforms["pw"]
   rusername = registuserinforms["name"]
   rusertel = registuserinforms["tel"]
   ruserinfo = registuserinforms["info"]
   cursor = connection.cursor()
   query_string = "insert into testsql_suser(suserid,suserpw,susername,susertel,sinfo) values(%s,%s,%s,%s,%s)"%(ruserid,ruserpw,rusername,rusertel,ruserinfo)
   cursor.execute(query_string)
   cursor.commit()

def insert2newuser(registuserinforms):
    ruserid =  registuserinforms["id"]
    ruserpw = registuserinforms["pw"]
    rusername = registuserinforms["name"]
    rusertel = registuserinforms["tel"]
    ruserinfo = registuserinforms["info"]
    with connection.cursor as cursor:
        try:
            #query_string = "insert into testsql_suser(suserid,suserpw,susername,susertel,sinfo) values(%s,%s,%s,%s,%s)",[ruserid,ruserpw,rusername,rusertel,ruserinfo]
            cursor.execute("insert into testsql_suser(suserid,suserpw,susername,susertel,sinfo) values(%s,%s,%s,%s,%s)",[ruserid,ruserpw,rusername,rusertel,ruserinfo])
            row = cursor.fetchall()
        except:
            pass
    return row

'''
#각각의 할아버지들의 아이디와 이름을 return
def ClientUser():
    cursor = connection.cursor()
    query_string = "select * from testsql_clientuser"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    cposts=[]
    for row in rows:
        dic = {'id' :row[1],'name':row[2]}
        cposts.append(dic)
    return cposts
'''
    
    



        
    