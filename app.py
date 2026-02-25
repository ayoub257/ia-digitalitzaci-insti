import streamlit as st
from groq import Groq

st.set_page_config(page_title="IA Digitalización 24/7", page_icon="🚀")

# Conectamos con la clave secreta que pondremos luego en Streamlit Cloud
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Falta la clave API en la configuración.")

st.title("🚀 Generador de Proyectos Pro")
st.write("Escribe un tema y la IA te dará una idea brillante.")

tema = st.text_input("¿Qué tema te interesa?")

if st.button("Generar"):
    if tema:
        with st.spinner('Pensando...'):
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Idea de proyecto sobre {tema}"}]
            )
            st.success("¡Hecho!")
            st.write(completion.choices[0].message.content)
