python
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from transformers import pipeline

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    response = chatbot(msg)
    send(response[0]['generated_text'], broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
