# app.py new
from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from flask_cors import CORS

# Configure the Gemini API key from an environment variable
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

app = Flask(__name__)
# CORS is needed to allow your frontend to talk to your backend during development
CORS(app)

@app.route('/api/check_grammar', methods=['POST'])
def check_grammar():
    try:
        data = request.get_json()
        user_text = data.get('text', '')

        if not user_text:
            return jsonify({"error": "No text provided."}), 400

        # This is your prompt for Gemini
        prompt = f"""
        You are a helpful grammar and spelling assistant. Review the following text for any errors.
        For each error you find, identify the mistake, provide the corrected version, and give a brief explanation of the rule.
        If there are no errors, simply say, "Your text is perfect!"

        Example:
        Text: "He go to the store."
        Analysis:
        - Mistake: Subject-verb agreement. The verb "go" should be "goes" to agree with the singular subject "He".
        - Corrected: He goes to the store.

        Your task:
        Text: "{user_text}"
        Analysis:
        """
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        # Format the response for a cleaner output
        response_text = response.text.replace('*', '').replace('**', '')
        
        return jsonify({"analysis": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
