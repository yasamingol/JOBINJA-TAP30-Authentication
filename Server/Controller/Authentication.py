from flask import Flask
app = Flask(__name__)

accountUserName = None
accountPassWord = None



@app.route('/postUsername/<string:username>')
def postUserName(username):
    # return escape(username)
    accountUserName = username
    return accountUserName




@app.route('/postPassword/<string:password>')
def postUserPassword(password):
    accountPassWord = password
    return accountPassWord


if __name__ == '__main__':
    app.run(host= "127.0.0.1",port="5000")

