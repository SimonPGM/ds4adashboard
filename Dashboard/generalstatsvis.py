import streamlit as st
import plotting

def stats_view(dfmedicine, dfuniques, visualization_mode):
    
    st.markdown("## Conteos generales del hospital respecto a los pacientes ingresados por trauma")
    
    metric_values = zip(dfuniques.iloc[:, 0].values, dfuniques.iloc[:, 1].values)
    metric_columns = st.columns(3)
    metric_count = 0

    for label, value in metric_values:
        metric_columns[metric_count].metric(label, value)
        metric_count += 1    
        
    barchart = plotting.group_comparisons_bar(dfmedicine, "Medicamento o Insumo", "Precio",
    "Comparativa de los precios de los medicamentos", "Costo")
    st.markdown("## Resumen del costo promedio de los medicamentos")
    
    if visualization_mode == "Gráfica":
        st.markdown("Haga click sobre el gráfico para obtener mayor información acerca del medicamento")
        st.plotly_chart(barchart)
    else:
        st.dataframe(dfmedicine)