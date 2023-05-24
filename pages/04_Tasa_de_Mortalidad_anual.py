import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

st.title("Tasa de Mortalidad Anual")
st.markdown("***")
st.markdown("#### Fórmula: all_fatalities / all_aboard * 100")
st.write("La Tasa de Mortalidad Anual se refiere a la proporción de fallecimientos en relación con una población o un conjunto de eventos durante un año determinado. Puede ser relevante en diferentes contextos, como la salud pública, la seguridad vial o la seguridad en el transporte. Al analizar este KPI, se pueden obtener insights sobre la evolución de la mortalidad a lo largo del tiempo y realizar comparaciones entre diferentes períodos o grupos de interés. Por ejemplo, en el ámbito de la salud, la Tasa de Mortalidad Anual puede ayudar a monitorear la efectividad de las políticas de prevención, evaluar el impacto de enfermedades o identificar áreas de mejora en la atención médica. En este caso nos ayuda a determinar posibles patrones entre los accidentes, fatales y no fatales y establecer relaciones en el pasado para prevenir a futuro.")

df = pd.read_csv('dataset_accidentes_prueba.csv', low_memory=False)

df['mortality_rate'] = (df['all_fatalities'] / df['all_aboard']) * 100


if st.checkbox("Puede visualizar el Dataframe aquí."):
    st.dataframe(df[['datetime', 'operator', 'all_aboard', 'all_fatalities', 'mortality_rate']])
if st.checkbox("Gráfico tasa mortalidad anual + media aritmética"):
    fig, ax = plt.subplots(figsize=(8, 6))
    df.groupby('year')['mortality_rate'].mean().plot(ax=ax, marker = "o")
    ax.axhline(df['mortality_rate'].mean(), color='r', linestyle='--', label='Media')
    plt.xlabel('Año')
    plt.ylabel('Tasa de Mortalidad de Pasajeros')
    plt.title('Tasa de Mortalidad de Pasajeros por Año')
    plt.legend()
    st.pyplot(fig)

media = df['mortality_rate'].mean()
st.markdown(f"- Media(%): {media:.2f}")

####
if st.checkbox("Reducción de la tasa de mortalidad (incompleto)"):
    df = df.sort_values('year')
    df['mortality_rate_diff'] = df['mortality_rate'].diff()
    df['mortality_rate_reduction'] = df['mortality_rate_diff'].fillna(0).cumsum()
    st.title('Reducción de la Tasa de Mortalidad Anual')
    st.write('Tendencia de la reducción de la tasa de mortalidad anual en comparación con el año anterior')
    start_year = st.number_input('Año inicial', min_value=int(df['year'].min()), max_value=int(df['year'].max()))
    end_year = st.number_input('Año final', min_value=int(start_year), max_value=int(df['year'].max()), value=int(df['year'].max()))
    df_filtered = df[(df['year'] >= start_year) & (df['year'] <= end_year)]
    fig, ax = plt.subplots()
    ax.plot(df_filtered['year'], df_filtered['mortality_rate_reduction'], marker='o', linestyle='-', color='blue')
    ax.set_xlabel('Año')
    ax.set_ylabel('Reducción de la Tasa de Mortalidad Anual')
    ax.set_title('Tendencia de la Reducción de la Tasa de Mortalidad Anual')
    fig.set_size_inches(10, 6)
    min_reduction = df_filtered['mortality_rate_reduction'].min()
    max_reduction = df_filtered['mortality_rate_reduction'].max()
    ax.set_ylim([min_reduction - 0.1 * abs(min_reduction), max_reduction + 0.1 * abs(max_reduction)])
    st.pyplot(fig)