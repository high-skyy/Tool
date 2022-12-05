from flask import Flask, request
import requests
import json

app = Flask("ping_container")

@app.route("/")
def greetings():
    return "[Sender_ping] Greetings! You have successfully pinged me"

@app.route("/ping")
def ping():
    response_message = "[sender_ping] ---ping-->"
    obj = {"message" : response_message}
    res = requests.get('http://127.0.0.1:5001/pong', data = json.dumps(obj))
    response_message += res.text

    f = open("E:/test/ping/test.txt", "w")
    f.write(response_message)
    f.close()

    return response_message


app.run(host = '127.0.0.1' , port = 5000)
