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
if st.button("Ver resultados"):
    puntaje = 0

    for i, p in enumerate(st.session_state.quiz):
        if respuestas_usuario[i] == p["respuesta"]:
            puntaje += 1

    st.success(f"Tu puntaje es: {puntaje}/4")
