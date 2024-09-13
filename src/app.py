# src/app.py

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from the .env file located in the root directory
load_dotenv(dotenv_path="../.env")

# Retrieve the API key from the environment variables
api_key = os.getenv("API_KEY")

if not api_key:
    raise Exception("API Key not found. Please set it in the .env file.")

# Configure the API key for Google Generative AI
genai.configure(api_key=api_key)

# Function to generate a response from the Google Generative AI
def generate_response(prompt):
    try:
        model = genai.GenerativeModel('gemini-1.0-pro-latest')
        response = model.generate_content(prompt)
        text_content = response.candidates[0].content.parts[0].text
        return text_content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Example usage (you can modify this to handle web requests, etc.)
if __name__ == "__main__":
    promptraw = input("Enter your prompt: ")
    prompt = promptraw + ", Give me a short description for resume that is ATS-friendly"
    response_text = generate_response(prompt)
    print(f"Response: {response_text}")
