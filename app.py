import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configure the API key for Google Generative AI
load_dotenv()

# Get the API key from the environment variable
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

# Get prompt input from the user
promptraw = input("Enter your prompt: ")
prompt = promptraw + ", Give me a short description for resume that is ATS-friendly"

# Generate and display the response
text_content = generate_response(prompt)
print(f"Response: {text_content}")
