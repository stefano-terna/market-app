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
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                x=0.7,
                y=1.2,
                buttons=[
                    dict(
                        label="Linea",
                        method="restyle",
                        args=[{"type": "scatter", "mode": "lines"}]
                    ),
                    dict(
                        label="Barre",
                        method="restyle",
                        args=[{"type": "bar"}]
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
