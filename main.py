import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/Worked dataset- DataSense.xlsx')

def miles_to_km(value):
    if isinstance(value, str) and "Miles" in value:
        try:
            parts = value.replace("Miles", "").strip()
            
            if "-" in parts:
                start, end = parts.split("-")
                start_km = round(float(start) * 1.60934, 1)
                end_km = round(float(end) * 1.60934, 1)
                return f"{start_km}-{end_km} km"
            else:
                return f"{round(float(parts) * 1.60934, 1)} km"
        except:
            return value
    return value

df["Commute Distance"] = df["Commute Distance"].apply(miles_to_km)

st.title("Análise de Público-Alvo - Bicicletas")


publico = df[df['Purchased Bike'] == "Yes"]

st.header("Público-Alvo")
st.write({
    "Idade média": round(publico["Age"].mean(), 2),
    "Renda média": round(publico["Income"].mean(), 2),
    "Região": publico["Region"].mode()[0],
    "Distância": publico["Commute Distance"].mode()[0],
})


st.header("Comparação")
not_buy = df[df['Purchased Bike'] == "No"]

st.write({
    "Idade (comprou)": round(publico["Age"].mean(), 2),
    "Idade (não comprou)": round(not_buy["Age"].mean(), 2),
    "Renda (comprou)": round(publico["Income"].mean(), 2),
    "Renda (não comprou)": round(not_buy["Income"].mean(), 2),
})


st.header("Taxa por Região")
regiao = df.groupby("Region")["Purchased Bike"].value_counts(normalize=True).unstack()

st.bar_chart(regiao)


st.header("Impacto da Distância")
distancia = df.groupby("Commute Distance")["Purchased Bike"].value_counts(normalize=True).unstack()

st.bar_chart(distancia)

st.header("Segmento Ideal")
segmento = df[
    (df["Age"] >= 30) &
    (df["Age"] <= 50) &
    (df["Commute Distance"].str.contains("0.0-1.6 km"))
]


st.write(segmento["Purchased Bike"].value_counts(normalize=True))