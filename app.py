import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import datetime

st.title('Visualizzatore di Dati di Mercato')

# Input dell'utente per selezionare il simbolo dell'azione
symbol = st.text_input('Inserisci il simbolo dell\'azione (es. TRN.MI):', 'TRN.MI')

# Utilizzo di yfinance per ottenere i dati
ticker_data = yf.Ticker(symbol)

# Visualizzazione di alcuni dati di base
st.write(ticker_data.info['longBusinessSummary'])

data = yf.download(symbol, period='10y')
data.reset_index(inplace=True)

# Grafico con Plotly Express
def create_line_chart(data, x_range=None):
    fig = px.line(data, x='Date', y='Close', title=f'Prezzo di chiusura: {ticker}')
    if x_range is not None:
        fig.update_xaxes(range=x_range)
    return fig

# Pulsanti per il reset e visualizzazione
st.title('Visualizzatore di Dati di Mercato con Streamlit e Plotly Express')

if st.button('YTD'):
    fig = create_line_chart(data, x_range=['2024-01-01', datetime.date.today().strftime('%Y-%m-%d')])
    st.plotly_chart(fig)
elif st.button('Mostra Tutto'):
    fig = create_line_chart(data)  # Nessun x_range specificato, mostra tutto
    st.plotly_chart(fig)
else:
    # Grafico di default al caricamento della pagina
    fig = create_line_chart(data)
    st.plotly_chart(fig)
