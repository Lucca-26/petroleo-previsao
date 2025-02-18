import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Modelo", page_icon="📈")

st.title("📈 Modelo de Previsão")

# 🔹 Coletar os dados do Yahoo Finance
brent_data = yf.Ticker("BZ=F").history(period="max")
brent_data.reset_index(inplace=True)

# 🔹 Remover fuso horário, se existir
if brent_data['Date'].dtype == "datetime64[ns, America/New_York]":
    brent_data['Date'] = brent_data['Date'].dt.tz_convert(None)

# 🔹 Identificar a última data disponível no dataset
last_date = brent_data["Date"].max()

# 🔹 Criar um filtro interativo com `slider` para ajustar o período da previsão
days_to_predict = st.sidebar.slider("Número de dias para prever:", min_value=1, max_value=30, value=7)

# 🔹 Criar variável target (preço de fechamento do próximo dia)
brent_data['Target'] = brent_data['Close'].shift(-1)

# 🔹 Remover linhas com valores NaN antes de separar X e y
brent_data.dropna(inplace=True)

# 🔹 Criar variáveis de entrada (X) e saída (y)
X = brent_data[['Open', 'High', 'Low', 'Close']]
y = brent_data['Target']

# 🔹 Treinar modelo de Regressão Linear
model = LinearRegression()
model.fit(X, y)

# 🔹 Previsão para os próximos N dias (a partir do último dia disponível)
future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=days_to_predict)

# Criar DataFrame fictício baseado no último dia do histórico
last_row = X.iloc[-1].values.reshape(1, -1)  # Última linha do histórico como base
future_predictions = []

for _ in range(days_to_predict):
    pred = model.predict(last_row)[0]  # Fazer a previsão
    future_predictions.append(pred)
    
    # Atualizar a última linha simulando uma continuidade dos dados
    last_row = np.array([[last_row[0][1], last_row[0][2], last_row[0][3], pred]])  # Shiftando valores

# Criar DataFrame para exibir as previsões com as datas futuras
df_predictions = pd.DataFrame({'Data': future_dates, 'Previsão': future_predictions})

# 🔹 Exibir previsões formatadas
st.write(f"### Previsão para os Próximos {days_to_predict} Dias")
df_predictions['Previsão'] = df_predictions['Previsão'].apply(lambda x: f"${x:.2f}")  # Adicionar símbolo de dólar e formatar
st.dataframe(df_predictions.set_index("Data"), width=500)

# 🔹 Gráfico interativo com previsão destacada em laranja
fig = px.line(brent_data, x="Date", y="Close", title="Preço Histórico e Previsão do Petróleo Brent", labels={'Close': 'Preço'})
fig.update_traces(name='Histórico', selector=dict(name='Close'))  # Renomear a linha do histórico
fig.add_scatter(x=df_predictions["Data"], y=df_predictions["Previsão"].str.replace('$', '').astype(float), mode="lines", name="Previsão", line=dict(color="orange", width=2))

st.plotly_chart(fig)

# Botões de navegação
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Voltar para Análise"):
        st.switch_page("main.py")

with col2:
    if st.button("➡ Próximo"):
        st.switch_page("pages/6_Conclusão.py")