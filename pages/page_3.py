import streamlit as st
from PIL import Image

import pandas as pd
import yfinance as yf

st.title('More Advance Level following from Youtube')

tickers= ('TSLA','AAPL','BTC-USD','ETH-USD')

dropdown= st.multiselect('Pick your assets',tickers)
start=st.date_input('Start',value=pd.to_datetime('2022-01-20'))
end=st.date_input('End',value=pd.to_datetime('today'))

def relativeret(df):
    rel=df.pct_change()
    cumret =(1+rel).cumprod() -1
    umret =cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    # =yf.download(dropdown,start,end)['Adj Close']
    df=relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)



