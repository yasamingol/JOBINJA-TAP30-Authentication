import sqlite3
import asyncio

c = sqlite3.connect('loginDB.db')
db = c.cursor()


async def createLoginTable():
     db.execute('''CREATE TABLE if not exists Logins
           (id INT PRIMARY KEY  NOT NULL,
           userId          TEXT             NOT NULL,
           loginToken      TEXT             NOT NULL,
           loginTime       TEXT             NOT NULL);''')
     print("Logins DB created successfully")


async def saveLogin(userId, loginToken, loginTime):
    id = await getNumberOfRowsOfLoginsTable()
    db.execute('INSERT INTO Logins VALUES (?,?,?,?)', (id, userId, loginToken, loginTime))
    print("login saved to DB successfully")
    c.commit()


async def getNumberOfRowsOfLoginsTable():
    rowCounter = 1
    return rowCounter


async def getLoginsFullDBTable():
    return db.execute('SELECT * FROM Logins').fetchall()


async def getLoginIdUsingToken(token):
    loginId = db.execute('SELECT id FROM Logins WHERE loginToken = ?', (token,)).fetchone()[0]
    return loginId


async def getAccountIdUsingToken(token):
    accountId = db.execute('SELECT userId FROM Logins WHERE loginToken = ? ', (token,)).fetchone()[0]
    return accountId


async def getLastLoginTokenId(accountId):
    tokenId = db.execute('SELECT id FROM Logins WHERE userId = ? ORDER BY loginTime DESC ', (accountId,)).fetchone()[0]
    return tokenId


if __name__ == '__main__':
    # asyncio.run(createLoginTable())
    # asyncio.run(saveLogin("0", "1234", "111"))
    asyncio.run(saveLogin("0", "123876786", "178711"))
    print(asyncio.run(getLastLoginTokenId("0")))