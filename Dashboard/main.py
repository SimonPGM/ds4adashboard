import streamlit as st
import pandas as pd
import gettinguniques
import introvis
import generalstatsvis
import costsvis

data_costos_medicamentos = pd.read_csv("ComparativaPrecios.csv")
data_costos_diagnosticos = pd.read_csv("TiempoPromedioDiagnosticos.csv")
data_conteos = pd.read_excel("Libro1.xlsx", sheet_name="Valores unicos")

unico_diagnosticos = gettinguniques.unique_values(data_costos_diagnosticos, "Diagnostico de Ingreso")
genero = gettinguniques.unique_values(data_costos_diagnosticos, "sexo")
eps = gettinguniques.unique_values(data_costos_diagnosticos, "EPS")

st.image("imgs/logo-HU_Horizontal_Azul.png")


st.sidebar.image("imgs/logo-HU_Horizontal_Azul.png")
st.sidebar.markdown("## Acá podrá encontrar las opciones adicionales que le permitirán interactuar con la applicación")
visualization_mode = st.sidebar.selectbox("Seleccione lo que desea ver",
    "-,Estadísticas Generales,Costos por trauma para las EPS".split(","))

if visualization_mode == "-":
    introvis.intro_view()

elif visualization_mode == "Estadísticas Generales":
    visualization_mode_stats = st.sidebar.radio("Seleccione el modo de vista de los datos", "Gráfica Tabla".split())
    generalstatsvis.stats_view(data_costos_medicamentos, data_conteos, visualization_mode_stats)

else:
    costsvis.costs_view(data_costos_diagnosticos, eps, genero, unico_diagnosticos)