# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:40:53 2024

@author: A393167
"""

### FUNCTIONS ###

def SMA(serie, periodo):
    ### funzione che calcola la media mobile di una serie per su un periodo
    return serie.rolling(periodo).mean()

def BBand(serie, periodo, k):
    ### funzione che calcola la Banda di Bollinger di una serie con largezza k*std
    ### dove k negativo da la banda inferiore e k>0 la superiore
    BB= SMA(serie,periodo)+k*serie.rolling(periodo).std()
    return BB
def Exp_max(serie):
    ## funzione che calcola il massimo assoluto in avanzamento della serie
    return serie.expanding().max()

def DonchianChannelUp(serie,periodo):
    # funzione che calcola il massimo relativo della serie in una finestra mobile
    return serie.rolling(periodo).max()

def DonchianChannelDown(serie,periodo):
    # funzione che calcola il minimo relativo della serie in una finestra mobile
    return serie.rolling(periodo).min()

def crossover(serie1,serie2):
    return (serie1>serie2) & (serie1.shift(1)<serie2.shift(1))

def crossunder(serie1,serie2):
    return (serie1<serie2) & (serie1.shift(1)>serie2.shift(1))