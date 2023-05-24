import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd 

st.title("Número de accidentes por operador")
st.markdown("***")
st.write("El número de accidentes por operador puede ser un KPI relevante en el ámbito de la seguridad aérea y la gestión de riesgos. Al monitorear y analizar la cantidad de accidentes asociados con cada operador, se puede evaluar la efectividad de las políticas, procedimientos y prácticas de seguridad implementadas por cada operador de la industria aérea. Este KPI puede proporcionar información importante sobre la seguridad y la gestión del riesgo en la operación de aeronaves, permitiendo identificar patrones, tendencias o áreas problemáticas específicas. Además, puede ayudar a establecer comparaciones entre operadores y a tomar decisiones informadas para mejorar la seguridad en la industria. También puede establecer relaciones geopoliticas. Algunas medidas importantes son:")
st.markdown("""
* *La empresa con más accidentes registrados es Aeroflot (Agencia Rusa).*
* *Las ciudades con las accidentes aereos son Moscow, New York y Manila.*
* *Hay 7 accidentes que no perteneces a ninguna entidad registrada, lo mas probable que vuelos ilegales*
""")


df = pd.read_csv('dataset_accidentes_prueba.csv', low_memory=False)

accidents_by_operator = df.groupby('operator').size().reset_index(name='total_accidents')

if st.checkbox("Aprete para el Dataframe"):
    st.dataframe(accidents_by_operator)
if st.checkbox("Apret para ver el graficos de accidentes por operador"):
    df_operador = df['operator'].value_counts().reset_index()
    df_operador.columns = ['operator', 'Cantidad de Accidentes']
    df_operador = df_operador.head(10)  
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_plot = ax.bar(df_operador['operator'], df_operador['Cantidad de Accidentes'], color='blue')
    plt.xlabel('Operadores')
    plt.ylabel('Cantidad de Accidentes')
    plt.title('Cantidad de Accidentes por Operador')
    plt.xticks(rotation=90)
    for rect in bar_plot:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height, str(int(height)),
            ha='center', va='bottom')
    st.pyplot(fig)

##########


if st.checkbox("Comparación con las Locaciones mas repetidas"):
    df_operador = df['operator'].value_counts().reset_index()
    df_operador.columns = ['operator', 'Cantidad de Accidentes']
    df_operador = df_operador.head(10)
    df_locaciones = df['location'].value_counts().reset_index()
    df_locaciones.columns = ['Locación', 'Cantidad de Accidentes']
    df_locaciones = df_locaciones.head(10) 
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Cantidad de Accidentes por Operador')
        fig, ax = plt.subplots(figsize=(10, 6))
        bar_plot = ax.bar(df_operador['operator'], df_operador['Cantidad de Accidentes'], color='blue')
        plt.xlabel('operator')
        plt.ylabel('Cantidad de Accidentes')
        plt.title('Cantidad de Accidentes por Operador')
        plt.xticks(rotation=90)
        for rect in bar_plot:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height, str(int(height)),
                    ha='center', va='bottom')
        st.pyplot(fig)
    with col2:
        st.subheader('Locaciones con Mayor Cantidad de Accidentes')
        st.table(df_locaciones)
