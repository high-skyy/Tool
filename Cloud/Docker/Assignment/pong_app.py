from flask import Flask, request
import requests
import json

app = Flask("pong_container")

@app.route("/")
def greetings():
    return "[Receiver_pong] Greetings! You have successfully pinged me"

@app.route("/pong")
def pong():
    params = json.loads(request.get_data())

    response_message = "[receiver_pong] Hi Hi Hi"
    full_message = ""
    full_message += params["message"]
    full_message += response_message

    f = open("E:/test/pong/test.txt", "w")
    f.write(full_message)
    f.close()

    return response_message

app.run(host = '127.0.0.1' , port = 5001)
