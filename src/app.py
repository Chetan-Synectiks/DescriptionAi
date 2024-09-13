from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Configure the API key for Google Generative AI
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

# Function to generate response from the Google Generative AI
def generate_response(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.0-pro-latest')
        response = model.generate_content(prompt)
        text_content = response.candidates[0].content.parts[0].text
        return text_content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Define a route for the API
@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', 'Give me a short description for resume that is ATS-friendly')
    response = generate_response(prompt)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
