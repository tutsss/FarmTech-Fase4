
import streamlit as st
import pandas as pd
import joblib
import datetime

# Carrega o modelo
modelo = joblib.load('modelo_irrigacao.joblib')

st.set_page_config(page_title="Dashboard FarmTech", layout="centered")

st.title("🌱 FarmTech Solutions - Previsão de Irrigação")

st.write("Insira os valores de umidade e nutrientes para prever se será necessário irrigar o solo.")

umidade = st.slider("Umidade do Solo (%)", 0, 100, 50)
nutrientes = st.slider("Níveis de Nutrientes (%)", 0, 100, 50)

dados_input = pd.DataFrame([[umidade, nutrientes]], columns=['umidade', 'nutrientes'])
previsao = modelo.predict(dados_input)[0]

if previsao == 1:
    st.error("💧 Irrigação NECESSÁRIA!")
else:
    st.success("✅ Solo com níveis adequados. Não irrigar.")

st.subheader("Dados analisados:")
st.dataframe(dados_input)

st.subheader("Exemplo de histórico:")
historico = pd.DataFrame({
    'Hora': [datetime.datetime.now().strftime("%H:%M")] * 5,
    'Umidade': [20, 25, 30, 50, umidade],
    'Nutrientes': [30, 35, 45, 60, nutrientes]
})
st.line_chart(historico[['Umidade', 'Nutrientes']])
