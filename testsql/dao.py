from django.db import connection

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
