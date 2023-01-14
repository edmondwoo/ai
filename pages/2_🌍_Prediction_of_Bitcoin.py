import streamlit as st
# First we will import the necessary Library 

import os
import pandas as pd
import numpy as np
import math
import datetime as dt
import matplotlib.pyplot as plt

# For Evalution we will use these library

from sklearn.metrics import mean_squared_error, mean_absolute_error, explained_variance_score, r2_score 
from sklearn.metrics import mean_poisson_deviance, mean_gamma_deviance, accuracy_score
from sklearn.preprocessing import MinMaxScaler

# For model building we will use these library

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import LSTM


# For PLotting we will use these library

import matplotlib.pyplot as plt
from itertools import cycle
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import pickle

class Toc:

    def __init__(self):
        self._items = []
        self._placeholder = None
    
    def title(self, text):
        self._markdown(text, "h1")

    def header(self, text):
        self._markdown(text, "h2", " " * 2)

    def subheader(self, text):
        self._markdown(text, "h3", " " * 4)

    def placeholder(self, sidebar=True):
        self._placeholder = st.sidebar.empty() if sidebar else st.empty()
    
    def placeholders(self, sidebar=False):
        self._placeholders = st.sidebar.empty() if sidebar else st.empty()

    def generate(self):
        if self._placeholder:
            self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)
    
    def _markdown(self, text, level, space=""):
        key = "".join(filter(str, text)).lower()
        print(text)
        key = key.replace(' ','-')
        key = key.replace('.','-')

        st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
        self._items.append(f"{space}* <a href='#{key}'>{text}</a>")

        
toc = Toc()

maindf=pd.read_csv('data/BTC-USD.csv')

toc.title('Prediction of Bitcoin')
# st.write('Cryptocurrency is a relatively new medium of exchange that’s gained popularity in the past decade. Crypto cheerleaders think the future of finance is cryptocurrency rather than stocks and conventional forms of currency, while others believe that the unregulated nature of cryptocurrency makes it too risky to support a full-fledged financial system. Cryptocurrencies lack government backing, and how much the market will bear determines their value.')
# st.write('Cryptocurrencies are maintained on decentralized networks of computers spread around the world. Strong cryptography provides security to transactions and storage, hence the term “cryptocurrency.” A cryptocurrency owner must use a password of at least 16 characters to gain access.')

# toc.header("Subheader 2")

model = tf.keras.models.load_model('data/my_model.h5')

with open('data/trainHistoryDict', "rb") as file_pi:
    history = pickle.load(file_pi)

loss = history.history['loss']
val_loss = history.history['val_loss']

print(loss)

epochs = range(len(loss))

plt.plot(epochs, loss, 'r', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend(loc=0)
fig=plt.figure(figsize=(9,8))


st.pyplot(fig)

toc.generate()