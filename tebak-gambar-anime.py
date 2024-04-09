#-----------------------------------------LIBRARY-----------------------------------------
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import torch
import requests
import io
import csv
from datetime import datetime
from PIL import Image
#--------------------------------------INISIASI MODEL-----------------------------------
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

API_URL = "https://api-inference.huggingface.co/models/cagliostrolab/animagine-xl-3.1"
headers = {"Authorization": "Bearer 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"}
#--------------------------------------ARTIFICIAL INTELLIGENCE-----------------------------------
# kesulitan = 
prompt = """User: Berikan saya satu karakter anime acak di website MyAnimeList,
kalau bisa yang umum, banyak orang tahu, outputnya hanya 2 atau 3 kata saja"""

def generate(prompt):
    response = model.generate_content(prompt)
    return response.text

a = generate(prompt)

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return io.BytesIO(response.content)

image_bytes = query({"inputs": a})

# Menyimpan hasil output ke dalam file CSV
output_file = 'generated_output.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([a])
    
#--------------------------------------FRONT-END-----------------------------------
st.markdown("## Tebak karakter anime, yang salah pindah agama")
st.image(Image.open(image_bytes))

user_input = st.text_input("Masukkan tebakan anda")
if user_input.lower() in prompt.lower():
    st.write("Selamat, Anda benar!")