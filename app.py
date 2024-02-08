import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import date

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
    fig = px.line(data, x='Date', y='Close', title=f'Prezzo di chiusura')
    if x_range is not None:
        fig.update_xaxes(range=x_range)
    return fig
    st.plotly_chart(fig)

# Sidebar o pulsanti principali
st.title('Visualizzatore di Dati di Mercato con Streamlit e Plotly Express')

# Opzione YTD
if st.button('YTD'):
    # Calcola la data di inizio dell'anno
    start_ytd = date(date.today().year, 1, 1).strftime('%Y-%m-%d')
    create_line_chart(data, x_range=[start_ytd, date.today().strftime('%Y-%m-%d')])
else:
    create_line_chart(data)
    
# Pulsante per mostrare tutto
if st.button('Mostra Tutto'):
    create_line_chart(data)
# Grafico di default al caricamento della pagina se nessun pulsante è premuto
else:
    create_line_chart(data)
