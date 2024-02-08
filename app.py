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

# Opzioni del menu nella sidebar
pagina = st.sidebar.selectbox("Seleziona una pagina:", ["Home", "Pagina 1", "Pagina 2"])

# Gestione della logica condizionale per mostrare le pagine
if pagina == "Home":
    st.header("Pagina Home")
    st.write("Benvenuto nella pagina Home!")
elif pagina == "Pagina 1":
    st.header("Pagina 1")
    st.write("Ecco alcune informazioni sulla Pagina 1.")
elif pagina == "Pagina 2":
    st.header("Pagina 2")
    st.write("Ecco alcune informazioni sulla Pagina 2.")

#definizione funzione data odierna
oggi=lambda:date.today()

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
                        args=[{"xaxis.range":[date(oggi().year, 1, 1),oggi()],"yaxis.autorange": True}]
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

# Sidebar o pulsanti principali
st.title('Visualizzatore di Dati di Mercato con Streamlit e Plotly Express')

create_line_chart(data)
