import streamlit as st
from PIL import Image

st.title('Kentaro App')
st.caption('This is my research')


col1, col2 =st.columns(2)
with col1:
 


 image =Image.open ('./data/IMG_2026.JPG')
 st.image(image,width=350)
 st.subheader('Introduction')
 st.text('My name is Kentaro Kamiya.')
 st.text('I have been living in New Zealand \n'
         'since 2011.I live here with my family')
 video_file= open('./data/ISYQ5032.mov','rb')
 video_bytes=video_file.read()
 st.video(video_bytes)
 
with col2:
 st.subheader('This is my sons')
 
 