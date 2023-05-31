from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi!! suresh this is a docker-file !!!'
