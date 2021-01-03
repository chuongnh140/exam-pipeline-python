#!/usr/bin/python3
from flask import Flask
import os
hostname = os.environ['HOST_NAMEE']
tag = os.environ['MY_TAG']
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World version is {0} hostname is {1}".format(tag,hostname)  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
