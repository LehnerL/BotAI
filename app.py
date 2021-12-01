#imports
from flask import Flask, render_template, request
import requests
import time

app = Flask(__name__)

#create chatbot
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": f"Bearer TOKEN"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

#activate this line in case model is still loading:
#time.sleep(3)


#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")

#bot response
def get_bot_response():
    userText = request.args.get('msg')
    output = query(userText)
    return str(output['generated_text'])


if __name__ == "__main__":
    app.run()
