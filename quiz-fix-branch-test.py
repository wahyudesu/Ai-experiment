#-----------------------------------------LIBRARY-----------------------------------------
import streamlit as st
import random
import google.generativeai as genai
import os
import json

from dotenv import load_dotenv

#--------------------------------------INISIASI MODEL-----------------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

#-----------------------------------------FRONT-END-----------------------------------------
st.title("Generator Quiz using Artificial Intelligence🗿🗿🗿🗿🗿")
jenis_soal = st.text_input("Masukkan soal apa yang ingin kamu kerjakan, TOEFL/UTBK/CPNS/MATEMATIKA/PENGETAHUAN UMUM: ")
tingkat_kesulitan = st.selectbox("Pilih tingkat kesulitan", ["gampang", "menengah", "sulit"])
session_state = st.session_state

#-----------------------------------------BACK-END-----------------------------------------
@st.cache(allow_output_mutation=True)
def generate_quiz(prompt):
    response = model.generate_content(prompt)
    json_output = response.text.replace('```', '').replace('json', '')
    with open('data.json', 'w') as file:
        file.write(json_output)

def open_quiz():
    with open('data.json', 'r') as file:
        json_output = file.read()
    data = json.loads(json_output)
    pertanyaan = data['pertanyaan']
    opsi = data['opsi_jawaban']
    jawaban = data['jawaban_benar']
    
    return pertanyaan, opsi, jawaban

if 'quiz_data' not in session_state:
    session_state.quiz_data = None

if st.button("Start"):
    soal = f"""User: Berikan saya satu pertanyaan beserta 4 opsi jawaban dan satu jawaban yang benar
    tentang {jenis_soal} dengan tingkat kesulitan {tingkat_kesulitan}, berikan dalam format JSON
    dengan 3 variabel yaitu pertanyaan, opsi_jawaban, dan jawaban_benar?"""
    generate_quiz(soal)
    session_state.quiz_data = open_quiz()

if session_state.quiz_data:
    pertanyaan, opsi, jawaban = session_state.quiz_data
    st.write("Pertanyaan:", pertanyaan)
    st.write("Opsi Jawaban:", opsi)
    st.write("Jawaban Benar:", jawaban)
