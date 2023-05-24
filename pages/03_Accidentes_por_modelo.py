
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd 
import plotly.graph_objects as go

st.title("Accidentes por Modelo de Avión")
st.markdown("### Douglas DC-3 y C-47")
st.markdown("***")
st.write("Al analizar este KPI, se pueden identificar modelos de avión que presenten una mayor incidencia de accidentes, lo cual puede indicar posibles problemas de diseño, mantenimiento o operación. Esto puede ayudar a las autoridades de aviación, fabricantes de aviones y operadores a tomar medidas correctivas, implementar mejoras en la seguridad y tomar decisiones informadas sobre la adquisición, uso y mantenimiento de los modelos de avión. Aunque se entiende que los modelos mas reptidos ciertamente son los modelos mas vendidos del siglo 20. Algunas metricas importantes a remarcar podrians ser:")
st.markdown("""
* *Los Modelos de la marca Douglas, DC-3, C-47 y C-47A son los que mas accidentes han tenido pero tambien son los aviones mas vendidos del siglo pasado.*
* *Existe un modelo que podría presentar un problema de fiabilidad en su performance, el Havilland DHC-6*
* *Se puede observar como ningun modelo persiste a dia de hoy en funcionamientos, siendo el ultimo en retirarse el DHC-6*
    """)

df = pd.read_csv('dataset_accidentes_prueba.csv', low_memory=False)
if st.checkbox("Grafico de Lineas - top 4 modelos"):
    modelos_top = df['ac_type'].value_counts().head(4).index.tolist()
    modelos_seleccionados = st.multiselect('Selecciona los Modelos de Avión', modelos_top)
    df_modelos = df[df['ac_type'].isin(modelos_seleccionados)]
    datos_modelos = df_modelos.groupby('year').size().reset_index(name='Cantidad_Accidentes')
    fig, ax = plt.subplots()
    ax.plot(datos_modelos['year'], datos_modelos['Cantidad_Accidentes'])
    ax.set_xlabel('Año')
    ax.set_ylabel('Cantidad de Accidentes')
    ax.set_title('Evolución de los Accidentes por Modelo de Avión')
    st.pyplot(fig)

####

if st.checkbox("Grafico de Lineas - todos los modelos"):
    modelos_avion = df['ac_type'].unique()
    figuras = {}
    for modelo in modelos_avion:
        df_modelo = df[df['ac_type'] == modelo]
        datos_modelo = df_modelo.groupby('year').size().reset_index(name='Cantidad_Accidentes')
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=datos_modelo['year'], y=datos_modelo['Cantidad_Accidentes'], name=modelo))
        fig.update_layout(title='Evolución de los Accidentes por Modelo de Avión', xaxis_title='Año', yaxis_title='Cantidad de Accidentes')
        figuras[modelo] = fig
    modelo_seleccionado = st.selectbox('Selecciona un Modelo de Avión', modelos_avion)
    figura_seleccionada = figuras[modelo_seleccionado]
    st.plotly_chart(figura_seleccionada)

#####

if st.checkbox("Comparación entre actvidad de los modelos a través del timepo"):
    modelos_mas_utilizados = df['ac_type'].value_counts().head(4).index.tolist()
    df_filtrado = df[df['ac_type'].isin(modelos_mas_utilizados)]
    datos_agrupados = df_filtrado.groupby(['ac_type', 'year']).size().unstack()
    plt.figure(figsize=(10, 6))
    for modelo in modelos_mas_utilizados:
        plt.plot(datos_agrupados.loc[modelo], label=modelo)
    plt.title('Evolución de los Accidentes por Modelo de Avión')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de Accidentes')
    plt.legend()
    st.pyplot(plt)