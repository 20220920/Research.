import streamlit as st
from PIL import Image

st.title('Kentaro App')
st.caption('This is my assingment')


col1, col2 =st.columns(2)
with col1:
 


 image =Image.open ('./data/IMG_2026.JPG')
 st.image(image,width=350)
 st.subheader('Introduction')
 st.text('My name is Kentaro Kamiya.')
 st.text('I have been living in New Zealand \n'
         'since 2011.I live in here with my family')
 
with col2:
 st.subheader('This is my sons')
 
 