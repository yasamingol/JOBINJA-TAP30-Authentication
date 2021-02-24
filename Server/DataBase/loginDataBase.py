import sqlite3
import asyncio

c = sqlite3.connect('loginDB.db')
db = c.cursor()


async def createConfirmationsTable():
     db.execute('CREATE TABLE Logins (id, userId, loginToken, loginTime)')
     print("Confirmation DB created successfully")


async def saveLogin(userId, loginToken, loginTime):
    db.execute('INSERT INTO Logins VALUES (?,?,?,?)', ("0", userId, loginToken, loginTime))
    print("login saved to DB successfully")
    c.commit()


async def getNumberOfRowsOfLoginsTable():
    rowCounter = 0
    return rowCounter


async def getLoginsFullDBTable():
    return db.execute('SELECT * FROM Logins').fetchall()


async def getLoginIdUsingToken(token):
    loginId = db.execute('SELECT id FROM Logins WHERE loginToken = ?', (token,))
    if loginId != None:
        return loginId.id

    else:
        return None


async def getAccountIdUsingToken(token):
    accountId = db.execute('SELECT userId FROM Logins WHERE loginToken = ? ', (token,))
    return accountId.userId


async def getLastLoginTokenId(accountId):
    tokenId = db.execute('SELECT id FROM Logins WHERE userId = ? ORDER BY loginTime DESC ', (accountId,))
    return tokenId.id


if __name__ == '__main__':
    # asyncio.run(createConfirmationsTable())
    asyncio.run(saveLogin("0", "1234", "111"))
    print(asyncio.run(getLoginsFullDBTable()))
