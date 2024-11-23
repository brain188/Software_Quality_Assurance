from flask import Flask, jsonify  

app = Flask(__name__)  

@app.route('/')  
def hello():  
    return jsonify(message="Hello, I am a level 400 student, this is software quality tools")