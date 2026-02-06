import streamlit as st
import random

# -----------------------------
# BASE DE DATOS (PREGUNTAS)
# -----------------------------
preguntas = [
    {
        "pregunta": "¿Qué busca principalmente la mejora continua en ingeniería industrial?",
        "opciones": ["Reducir la calidad", "Optimizar procesos constantemente", "Aumentar errores"],
        "respuesta": "Optimizar procesos constantemente"
    },
    {
        "pregunta": "¿Cuál es una herramienta común en mejora continua?",
        "opciones": ["Diagrama de Pareto", "Tabla periódica", "Mapa político"],
        "respuesta": "Diagrama de Pareto"
    },
    {
        "pregunta": "¿Qué significa el ciclo PDCA?",
        "opciones": ["Planear, Hacer, Verificar, Actuar", "Producir, Diseñar, Controlar, Analizar", "Pensar, Decidir, Crear, Aplicar"],
        "respuesta": "Planear, Hacer, Verificar, Actuar"
    },
    {
        "pregunta": "¿Cuál es el objetivo del Lean Manufacturing?",
        "opciones": ["Eliminar desperdicios", "Aumentar inventario", "Reducir productividad"],
        "respuesta": "Eliminar desperdicios"
    },
    {
        "pregunta": "¿Qué representa Kaizen?",
        "opciones": ["Cambio continuo y mejora", "Producción masiva", "Automatización total"],
        "respuesta": "Cambio continuo y mejora"
    },
    {
        "pregunta": "¿Para qué sirve un diagrama de flujo?",
        "opciones": ["Decoración visual", "Representar procesos paso a paso", "Guardar archivos"],
        "respuesta": "Representar procesos paso a paso"
    },
    {
        "pregunta": "¿Qué busca la estandarización de procesos?",
        "opciones": ["Variabilidad", "Consistencia en resultados", "Confusión operativa"],
        "respuesta": "Consistencia en resultados"
    },
    {
        "pregunta": "¿Qué herramienta ayuda a identificar causas raíz?",
        "opciones": ["Diagrama Ishikawa", "Calendario", "Regla de cálculo"],
        "respuesta": "Diagrama Ishikawa"
    },
    {
        "pregunta": "¿Qué significa KPI?",
        "opciones": ["Indicador clave de desempeño", "Proceso industrial básico", "Sistema eléctrico"],
        "respuesta": "Indicador clave de desempeño"
    },
    {
        "pregunta": "¿Cuál es un beneficio de mejorar procesos?",
        "opciones": ["Mayor eficiencia", "Más desperdicio", "Menos control"],
        "respuesta": "Mayor eficiencia"
    }
]

# -----------------------------
# INTERFAZ STREAMLIT
# -----------------------------
st.title("Quiz: Procesos y Mejora Continua en Ingeniería Industrial")

# Seleccionar 4 preguntas aleatorias
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

# Botón verificar
if st.button("Ver resultados"):
    puntaje = 0

    for i, p in enumerate(st.session_state.quiz):
        if respuestas_usuario[i] == p["respuesta"]:
            puntaje += 1

    st.success(f"Tu puntaje es: {puntaje}/4")

