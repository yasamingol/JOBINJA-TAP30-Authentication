import sqlite3

c = sqlite3.connect('loginDB.db',check_same_thread=False)
db = c.cursor()



# logins table
async def createLoginTable():
     db.execute('''CREATE TABLE if not exists Logins
           (id INT PRIMARY KEY  NOT NULL,
           username          TEXT             NOT NULL,
           loginToken      TEXT             NOT NULL,
           loginTime       TEXT             NOT NULL);''')
     print("Logins DB created successfully")


async def saveLogin(username, loginToken, loginTime):
    numberOfRows = await getNumberOfRowsOfLoginsTable()
    db.execute('INSERT INTO Logins VALUES (?,?,?,?)', (numberOfRows, username, loginToken, loginTime))
    print("login saved to DB successfully")
    c.commit()


async def getNumberOfRowsOfLoginsTable():
    numberOfRows = len(db.execute('SELECT * FROM Logins').fetchall())
    return numberOfRows


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




#   accounts table
async def createAccountsTable():
    db.execute('''CREATE TABLE if not exists Accounts
           (id INT PRIMARY KEY  NOT NULL,
           username          TEXT             NOT NULL,
           password      TEXT             NOT NULL);''')
    return "Accounts DB created successfully"


async def saveAccount(username,password):
    numberOfRows = await getNumberOfRowsOfAccountsTable()
    db.execute('INSERT INTO Accounts VALUES (?,?,?)', (numberOfRows, username, password))
    print( "account saved to DB successfully")
    c.commit()



async def getAccountsFullDBTable() :
    allAccountsList = db.execute('SELECT * FROM Accounts').fetchall()
    return allAccountsList



async def getFullAccountById(accountId):
    return db.execute('SELECT * FROM Accounts WHERE id = ?',(accountId,)).fetchall()[0]


async def getAccountUsernameUsingAccountId(accountID):
    return db.execute ('SELECT username FROM Accounts WHERE id = ?', (accountID,)).fetchone()[0]


async def getAccountPasswordUsingAccountId(accountID):
    return db.execute ('SELECT password FROM Accounts WHERE id = ?', (accountID,)).fetchone()[0]



async def getAccountIDUsingAccountUsername(accountUsername) :
    return db.execute ('SELECT id FROM Accounts WHERE username = ?', (accountUsername,)).fetchone()[0]



async def getNumberOfRowsOfAccountsTable() :
    numberOfRows = len(db.execute('SELECT * FROM Accounts').fetchall())
    return numberOfRows



