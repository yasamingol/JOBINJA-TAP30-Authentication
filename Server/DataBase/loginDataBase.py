import sqlite3

c = sqlite3.connect('loginDB.db',check_same_thread=False)
db = c.cursor()


async def createLoginTable():
     db.execute('''CREATE TABLE if not exists Logins
           (id INT PRIMARY KEY  NOT NULL,
           username          TEXT             NOT NULL,
           loginToken      TEXT             NOT NULL,
           loginTime       TEXT             NOT NULL);''')
     print("Logins DB created successfully")


async def saveLogin(username, loginToken, loginTime):
    if await getNumberOfRowsOfLoginsTable()==-1:
        id = 0
    else:
        id = await getNumberOfRowsOfLoginsTable()

    db.execute('INSERT INTO Logins VALUES (?,?,?,?)', (id, username, loginToken, loginTime))
    print("login saved to DB successfully")
    c.commit()


async def getNumberOfRowsOfLoginsTable():
    rowCounter = db.rowcount
    return rowCounter


async def getLoginsFullDBTable():
    return db.execute('SELECT * FROM Logins').fetchall()


async def getLoginIdUsingToken(token):
    loginId = db.execute('SELECT id FROM Logins WHERE loginToken = ?', (token,)).fetchone()[0]
    return loginId


async def getAccountIdUsingToken(token):
    username = db.execute('SELECT username FROM Logins WHERE loginToken = ? ', (token,)).fetchone()[0]
    return username


async def getLastLoginTokenId(username):
    tokenId = db.execute('SELECT id FROM Logins WHERE username = ? ORDER BY loginTime DESC ', (username,)).fetchone()[0]
    return tokenId

async def checkIfTokenExists(token):
    db.execute("SELECT id FROM Logins WHERE loginToken = ?", (token,))
    data = db.fetchall()
    if len(data) == 0:
        return False
    else:
        return True