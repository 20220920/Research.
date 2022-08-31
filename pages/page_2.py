import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Ethrium-USD 5days data by using Excel')
df=pd.read_csv('./data/ETH-USD.csv')

st.dataframe(df)

st.line_chart(df['High'])
st.bar_chart(df['Low'])

fig,ax=plt.subplots()
ax.plot(df.index, df['Adj Close'])
ax.set_title ('matplotlib graph')
st.pyplot(fig)