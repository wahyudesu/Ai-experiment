#-----------------------------------------LIBRARY-----------------------------------------
import streamlit as st
import random
import google.generativeai as genai

from dotenv import load_dotenv

import os
import pathlib
import textwrap
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
#-----------------------------------------FRONT-END------------------------------
pertanyaan = "### " + pertanyaan
st.markdown(pertanyaan)

left_column, tengah_column, right_column = st.columns(3)

with left_column:
    button1 = st.button(opsi[0])
    button2 = st.button(opsi[1])
with tengah_column:
    button3 = st.button(opsi[2])
    button4 = st.button(opsi[3])
#-----------------------------------------OUTPUT----------------------------------------
if button1 or button2 or button3 or button4:
    correct = False
    if button1 and opsi[0] == jawaban:
        correct = True
    elif button2 and opsi[1] == jawaban:
        correct = True
    elif button3 and opsi[2] == jawaban:
        correct = True
    elif button4 and opsi[3] == jawaban:
        correct = True

    if correct:
        st.write("Correct!")
        st.image("https://i.pinimg.com/originals/11/c7/6f/11c76fb123c8e1026659d39638ba2e82.png",width= 300)
    else:
        st.write("Wrong!")
        st.image("https://i.pinimg.com/564x/c2/41/6f/c2416f20691040610594b33f53f016b1.jpg", width=300)