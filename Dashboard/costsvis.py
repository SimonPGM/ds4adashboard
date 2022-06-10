import streamlit as st
import plotting

def costs_view(df, eps_values, gender_values, diagnostic_values):
    eps = st.sidebar.selectbox("Seleccione la EPS para la cual desea ver el costo promedio", eps_values)
    gender = st.sidebar.selectbox("Seleccione el genero de los pacientes para el que desea ver el costo promedio", gender_values)
    diagnostic = st.selectbox("Seleccione el genero de los pacientes para el que desea ver el costo promedio", diagnostic_values)

    st.markdown(f"## Información para los pacientes ingresados por {diagnostic.lower()}")
    line_chart = plotting.plot_cost(df, "Costo", "EPS", "sexo", "Diagnostico de Ingreso", eps, "Días internados",
    diagnostic, gender, "Gráfico de costos acumulados")
    if line_chart is None:
        st.markdown("No se encuentra información disponible para mostrar con los filtros seleccionados")
    else:
        st.plotly_chart(line_chart)
