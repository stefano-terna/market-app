import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import date

#definizione funzione data odierna
oggi=date.today()
# Grafico con Plotly Express
def create_line_chart(data, x_range=None):
    fig = px.line(data, x='Date', y='Close', title=f'Prezzo di chiusura')
    if x_range is not None:
        fig.update_xaxes(range=x_range)
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                buttons=[
                    dict(
                        label="YTD",
                        method="relayout",
                        args=[{"xaxis.range":["2024-01-01",None],"yaxis.autorange": True}]
                    ),
                    dict(
                        label="Mostra tutto",
                        method="relayout",
                        args=[{"xaxis.autorange": True, "yaxis.autorange": True}]
                    )
                ]
            )
        ]
    )
    st.plotly_chart(fig)
    return fig

st.title('Visualizzatore di Dati di Mercato')

# Input dell'utente per selezionare il simbolo dell'azione
symbol = st.text_input('Inserisci il simbolo dell\'azione (es. TRN.MI):', 'TRN.MI')

# Utilizzo di yfinance per ottenere i dati
ticker_data = yf.Ticker(symbol)



data = yf.download(symbol, period='10y')
data.reset_index(inplace=True)

# Inizializzazione dello stato della pagina se non esiste
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Home"

# Funzioni per impostare la pagina
def set_home():
    st.session_state.pagina = "Home"

def set_pagina1():
    st.session_state.pagina = "Market Data"

def set_pagina2():
    st.session_state.pagina = "Snam"

# Pulsanti nella sidebar per selezionare la pagina
st.sidebar.button("Home", on_click=set_home)
st.sidebar.button("Market Data", on_click=set_pagina1)
st.sidebar.button("Snam", on_click=set_pagina2)

# Titolo dell'applicazione
st.title("Applicazione Streamlit con Sidebar")

# Mostra la pagina selezionata
if st.session_state.pagina == "Home":
    st.header("Pagina Home")
    st.write("Benvenuto nella pagina Home!")
    
    # Visualizzazione di alcuni dati di base
    st.write(ticker_data.info['longBusinessSummary'])
    
elif st.session_state.pagina == "Market Data":
    st.header("Market Data")
    st.write("Ecco alcune informazioni sui dati di mercato.")
    
    # Sidebar o pulsanti principali
    st.title('Visualizzatore di Dati di Mercato con Streamlit e Plotly Express')
    create_line_chart(data)

elif st.session_state.pagina == "Snam":
    st.header("Snam")
    st.write("Ecco alcune informazioni sulla Snam.")
    symbol_1 = st.text_input('Inserisci il simbolo dell\'azione (es. SRG.MI):', 'SRG.MI')

    # Utilizzo di yfinance per ottenere i dati
    ticker_data = yf.Ticker(symbol_1)
    data_1 = yf.download(symbol_1, period='10y')
    data_1.reset_index(inplace=True)

    # Sidebar o pulsanti principali
    st.title('Visualizzatore di Dati di Mercato con Streamlit e Plotly Express')
    create_line_chart(data_1)







