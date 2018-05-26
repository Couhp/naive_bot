from flask import Flask
from flask import request, json
from pymessenger.bot import Bot
import requests
app = Flask(__name__)

ACCESS = "EAAB8i2fNMN8BAHNuHYu8Rs8x1qszrEnlpPgamXlwkFwsBCrao8lKZBa90I29F6XblbhZBeA9xCxqZCms0ZCqZCcIxb1lpc2SP1ke8b6J3JyQnxms4ZAkZAREY5LgWLHDieUeqPWigZCEZBSWThx8AFVxfoANaeAFL3gWLfv7dJAY6M9jXbt5oz9zT"
bot = Bot(ACCESS)



@app.route('/', methods=['GET'])
def hello_world():
    user = request.args.get('hub.challenge')
    return user


@app.route('/', methods=['POST'])
def chat():
    print (json.loads(request.data))
    data = json.loads(request.data)
    id = data["entry"][0]["messaging"][0]["sender"]["id"]
    text_msg = data["entry"][0]["messaging"][0]['message']['text']
    print (id)
    bot.send_text_message(id, text_msg)
    
    
    return "ok"


app.run(port=8080, host="0.0.0.0")