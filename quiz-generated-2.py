#-----------------------------------------LIBRARY-----------------------------------------
import streamlit as st
import random
import google.generativeai as genai

from dotenv import load_dotenv

import os
import google.generativeai as genai
import pandas as pd
import json

from IPython.display import display
from IPython.display import Markdown

#--------------------------------------INISIASI MODEL-----------------------------------
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

#-----------------------------------------FRONT-END-----------------------------------------
pertanyaan = "## " + ("Generator Quiz using Artificial Intelligence🗿🗿🗿🗿🗿")
st.markdown(pertanyaan)
jenis_soal = st.text_input("Masukkan soal apa yang ingin kamu kerjakan, TOEFL/UTBK/CPNS/MATEMATIKA/PENGETAHUAN UMUM: ")
tingkat_kesulitan = st.selectbox("Pilih tingkat kesulitan", ["gampang", "menengah", "sulit"])
#-----------------------------------------BACK-END-----------------------------------------

soal = f"""User: Berikan saya satu pertanyaan beserta 4 opsi jawaban dan satu jawaban yang benar
tentang {jenis_soal} dengan tingkat kesulitan {tingkat_kesulitan}, berikan dalam format JSON
dengan 3 variabel yaitu pertanyaan, opsi_jawaban, dan jawaban_benar?"""

# prompt = soal + "Gemini: []"

def generate_quiz(prompt):
    response = model.generate_content(prompt)
    json_output = response.text.replace('```', '').replace('json', '')

    with open('data.json', 'w') as file:
        file.write(json_output)

with open('data.json', 'r') as file:
    json_output = file.read()

def open_quiz(json_output):
    data = json.loads(json_output)
    pertanyaan = data['pertanyaan']
    opsi = data['opsi_jawaban']
    jawaban = data['jawaban_benar']
    
    return pertanyaan, opsi, jawaban

generate_quiz(soal)
open_quiz(json_output)