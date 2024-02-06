import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Visualizzatore di Dati di Mercato')

# Input dell'utente per selezionare il simbolo dell'azione
symbol = st.text_input('Inserisci il simbolo dell\'azione (es. TRN.MI):', 'TRN.MI')

# Utilizzo di yfinance per ottenere i dati
data = yf.Ticker(symbol)

# Visualizzazione di alcuni dati di base
st.write(data.info['longBusinessSummary'])

# Ottenere e visualizzare i dati storici
hist_data = data.history(period="1mo")  # dati dell'ultimo mese
st.line_chart(hist_data['Close'])
