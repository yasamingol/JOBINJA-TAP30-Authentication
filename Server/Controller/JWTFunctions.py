# requirments
from datetime import date, datetime, time
import jwt
from Server.DataBase.loginDataBase import *
import asyncio






# token
async def generateJWT(username, password):
    user = {
        "username": username,
        "password": password
    }
    jwt_valid_seconds = 180
    expiryTime = round(datetime.now().timestamp()) + jwt_valid_seconds
    payload = {"some": "payload", "aud": user, "exp": expiryTime}
    token = jwt.encode(payload, "secret")
    return token.decode()


async def checkIfTokenIsExpired(token):
    decodedToken = jwt.decode(token, verify=False)
    currentTime = round(datetime.now().timestamp())
    tokenExp = decodedToken.get('exp')
    return currentTime > tokenExp


async def checkTokenValidation(token):
    if await checkIfTokenExists(token):
        tokenId = await getLoginIdUsingToken(token)
        isExpired = await checkIfTokenIsExpired(token)
        isLatestLogin = await checkIfTokenIsForTheLatestLogin(token, tokenId)
        if isExpired:
            isValid = False,
            message = "token has expired!"
            return isValid, message

        elif isLatestLogin != True:
            isValid = False
            message = "this is not your latest login! updated version of token is required."
            return isValid, message

        else:
            isValid = True
            message = "token is valid."
            return isValid, message

    else:
        isValid = False,
        message = "token is undefined!"
        return isValid, message


async def checkIfTokenIsForTheLatestLogin(token, tokenId):
    accountId = await getAccountIdUsingToken(token)
    latestTokenId = await getLastLoginTokenId(accountId)
    if latestTokenId == tokenId:
        return True
    else:
        return False


async def validateLoginToken(token):
    isValid,message = await checkTokenValidation(token)
    if (isValid):
        isValid: True
        message: message
        return isValid, message

    else:
        isValid: False
        message: message
        return isValid, message

if __name__ == '__main__':
    asyncio.run(createLoginTable())
