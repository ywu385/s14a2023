from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!  Welcome to S14a2023</p>"

@app.route("/datetime")
# show the current date time in the server's timezone and another datetime in the UTC timezone

@app.route("/usertimezone")
#  third one for your own timezone with the location you are currently at
