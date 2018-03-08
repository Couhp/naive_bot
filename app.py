from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    user = request.args.get('hub.challenge')
    return user


app.run(port=8080, host="0.0.0.0")