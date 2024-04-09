import os
import google.generativeai as genai
import json
from dotenv import load_dotenv

def generate_quiz(prompt):
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    json_output = response.text.replace('```', '').replace('json', '')

    with open('json.json', 'w') as file:
        file.write(json_output)

    return json_output