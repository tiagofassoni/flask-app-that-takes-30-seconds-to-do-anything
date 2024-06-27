from flask import Flask
from time import sleep

app = Flask(__name__)

@app.route("/")
def hello_world():
    sleep(30)
    return "30 seconds have passed"

@app.route("/goddammit")
def goddammit():
    return "It is not you, it is render.com"