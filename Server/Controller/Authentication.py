from flask import Flask,request,jsonify
app = Flask(__name__)

accountUserName = None
accountPassWord = None



@app.route('/getUsername/<string:username>')
def getUserName(username):
    # return escape(username)
    accountUserName = username
    return accountUserName




@app.route('/getPassword/<string:password>')
def getUserPassword(password):
    accountPassWord = password
    return accountPassWord


@app.route('login')


if __name__ == '__main__':
    app.run(host= "127.0.0.1",port="5000")

