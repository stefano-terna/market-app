import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

st.title('Visualizzatore di Dati di Mercato')

# Input dell'utente per selezionare il simbolo dell'azione
symbol = st.text_input('Inserisci il simbolo dell\'azione (es. TRN.MI):', 'TRN.MI')

# Utilizzo di yfinance per ottenere i dati
ticker_data = yf.Ticker(symbol)

# Visualizzazione di alcuni dati di base
st.write(ticker_data.info['longBusinessSummary'])

data = yf.download(symbol, period='10y')
data.reset_index(inplace=True)

# Funzione per creare il grafico
def create_chart(x_range=None):
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                    open=data['Open'], high=data['High'],
                    low=data['Low'], close=data['Close'])])

    fig.update_layout(xaxis_rangeslider_visible=True)

    if x_range:
        fig.update_xaxes(range=x_range)

    return fig

# Pulsanti per il reset
if st.button('Reset a Gennaio 2021'):
    fig = create_chart(x_range=['2021-01-01', '2021-01-31'])
    st.plotly_chart(fig)
elif st.button('Mostra Tutto'):
    fig = create_chart()  # Nessun x_range specificato, mostra tutto
    st.plotly_chart(fig)
else:
    # Grafico di default al caricamento della pagina
    fig = create_chart()
    st.plotly_chart(fig)


