from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi!! Jerry kuruvi this is a docker-file!'
