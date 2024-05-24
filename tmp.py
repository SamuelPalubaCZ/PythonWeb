from main import *
from flask import Flask
XDD = weather_tempature(weather_dowland("Warsaw"))
app = Flask(__name__)

@app.route('/')
def hello():
    return XDD

if __name__ == '__main__':
    app.run()
