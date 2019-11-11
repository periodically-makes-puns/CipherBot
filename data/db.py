import sqlite3

def readplaintext(userid):
    conn = sqlite3.connect('data/users.db')
    cursor = conn.execute("SELECT * FROM Users WHERE USERID = ?", (userid,))
    for row in cursor:
        return row[1]

def writeplaintext(userid,plaintext):
    conn = sqlite3.connect('data/users.db')
    cursor = conn.execute("SELECT * FROM Users WHERE USERID = ?", (userid,))
    if(cursor.fetchone != None):
        conn.execute("UPDATE Users SET PLAINTEXT = ? WHERE USERID = ?", (plaintext, userid))
    if(cursor.fetchone() == None):
        conn.execute("INSERT INTO Users (USERID,PLAINTEXT) VALUES (?, ?);", (userid, plaintext))
    
    conn.commit()

def readalldata():
    conn = sqlite3.connect('data/users.db')
    cursor = conn.execute("SELECT * FROM Users")
    return cursor