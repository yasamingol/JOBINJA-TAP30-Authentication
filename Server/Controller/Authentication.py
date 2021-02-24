from flask import Flask,request,jsonify
app = Flask(__name__)

accountUserName = None
accountPassWord = None
loginToken = None

@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        accountUserName = request.json.get('username')
        accountPassWord = request.json.get('password')
        return createToken(accountUserName,accountPassWord)




def createToken(username,password):
    #actual token creator
    loginToken = username+password
    return loginToken

if __name__ == '__main__':
    app.run(host= "127.0.0.1",port="5000")

