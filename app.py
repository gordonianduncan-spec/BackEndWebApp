# app.py
print("Application is starting...")  # Add this line

from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from flask_cors import CORS

# Configure the Gemini API key from an environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

app = Flask(__name__)
# CORS is needed to allow your frontend to talk to your backend
CORS(app)

@app.route('/api/check_grammar', methods=['POST'])
def check_grammar():
    print("Received request to check grammar...")  # Add this line
    try:
        data = request.get_json()
        user_text = data.get('text', '')
        # ... rest of your code
