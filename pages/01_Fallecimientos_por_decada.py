import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd 

st.title("Fallecimientos por década")
st.markdown("***")
st.write(" La cantidad de fallecidos en accidentes de aviación es una métrica fundamental para evaluar la seguridad y el impacto de estos incidentes. Al analizar esta métrica a lo largo de las décadas, podemos obtener información sobre la tendencia de la seguridad en la industria de la aviación a lo largo del tiempo. Este KPI ayuda a determinar patrones y tendencias a traves de la décadas para aplicar acciones correctivas. Algunos datos importantes a recalcar sobre este KPI:")
st.markdown("""
* *Las décadas con mas accidentes ha sido la de 1960, 1950 y 1990.* 
* *La década con mas accidentes fatales ha sido 1960.*
""")
df = pd.read_csv("dataset_accidentes_prueba.csv", low_memory=False)

fig, ax = plt.subplots(figsize=(10, 6))
decadas_disponibles = range(df['year'].min() // 10 * 10, df['year'].max(), 10)
decada_seleccionada = st.slider('Selecciona una década:', min_value=min(decadas_disponibles), max_value=max(decadas_disponibles), step=10, value=1960)

datos_filtrados = df[df['year'].between(decada_seleccionada, decada_seleccionada + 9)]
datos_agrupados = datos_filtrados.groupby('year')['all_fatalities'].sum()
datos_agrupados.plot(marker='o', linestyle='-', ax=ax)

ax.set_xlabel('Año')
ax.set_ylabel('Cantidad de Fallecidos')
ax.set_title('Cantidad de Fallecidos por Año')

st.pyplot(fig)