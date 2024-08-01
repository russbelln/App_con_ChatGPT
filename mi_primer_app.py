import streamlit as st

# Título y autor de la app
st.title("Mi primera app")
st.write("Esta app fue elaborada por “RUSSBELL NOREÑA MEJIA”.")

# Pregunta al usuario por su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Verifica si el usuario ingresó un nombre
if nombre_usuario:
    mensaje_bienvenida = f"{nombre_usuario}, te doy la bienvenida a mi primera app."
    st.write(mensaje_bienvenida)
    st.write(mensaje_bienvenida)
