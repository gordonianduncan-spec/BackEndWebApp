from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "OK", "message": "Hello from the Python backend!"})

if __name__ == '__main__':
    app.run(debug=True)
