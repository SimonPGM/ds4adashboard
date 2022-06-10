import streamlit as st

def intro_view():
    st.markdown("En esta aplicación podra llevar seguimiento de las estadísticas generales de los pacientes \
    ingresados por trauma al hospital, costos asociados a medicamentos y costo por paciente según su género, su EPS y \
        la clase de trauma que este presente.")
    st.markdown("Para interactuar con la aplicación despliegue el menú de la flecha que se encuentra en \
        la parte superior izquierda.")
    st.image("imgs/hospital_logo.jpg")