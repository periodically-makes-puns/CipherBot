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
        conn.execute("INSERT INTO Users (USERID,PLAINTEXT,SCORE) VALUES (?, ?, ?);", (userid, plaintext, 0))
    
    conn.commit()

def changescore(userid,increment):
    conn = sqlite3.connect('data/users.db')

    cursor = conn.execute("SELECT * FROM Users WHERE USERID = ?", (userid,))
    for row in cursor:
        score = row[2]
    
    score += increment
    conn.execute("UPDATE Users SET SCORE = ? WHERE USERID = ?", (score, userid))
    conn.commit()

def readallscores():
    scores = []
    conn = sqlite3.connect('data/users.db')
    cursor = conn.execute("SELECT * FROM Users")
    for row in cursor:
        scores.append([row[0],row[2]])
    
    return scores