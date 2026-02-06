import streamlit as st
import random
import json

# -----------------------------
# CARGAR PREGUNTAS DESDE JSON
# -----------------------------
with open("preguntas.json", "r", encoding="utf-8") as file:
    preguntas = json.load(file)

st.title("Quiz: Procesos y Mejora Continua en Ingeniería Industrial")

# -----------------------------
# INGRESAR NOMBRE
# -----------------------------
if "nombre" not in st.session_state:
    st.session_state.nombre = ""

nombre_input = st.text_input("Ingresa tu nombre:")

if nombre_input:
    st.session_state.nombre = nombre_input

# -----------------------------
# BOTÓN REINICIAR QUIZ
# -----------------------------
if st.button("Reiniciar Quiz"):
    st.session_state.clear()
    st.rerun()

# -----------------------------
# SELECCIONAR 4 PREGUNTAS RANDOM
# -----------------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = random.sample(preguntas, 4)

respuestas_usuario = []

# Mostrar preguntas
for i, p in enumerate(st.session_state.quiz):
    st.subheader(f"Pregunta {i+1}")
    respuesta = st.radio(
        p["pregunta"],
        p["opciones"],
        key=i
    )
    respuestas_usuario.append(respuesta)

# -----------------------------
# VER RESULTADOS
# -----------------------------
