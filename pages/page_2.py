import streamlit as st
import pandas as pd
st.title('main_app.py code')
code='''
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
 '''
st.code(code,language='python')
 
 
st.title('Page_1.py Code')
code='''
st.title('Widget')
with st.form(key='profile_form'):
 name= st.text_input('Name')
 
 gender_category=st.radio(
     'Gender',
     ('Man','Woman')
 )
 hobby=st.multiselect(
     'Hobby',
     ('Sport','Anime','Movie','Fishing','Cooking','etc')
 )
 height=st.slider('Height',min_value=110, max_value=210)

 submit_btn= st.form_submit_button('Send')
 cancel_btn= st.form_submit_button('Cancel')
 if submit_btn:
    st.text(f'Hello!{name}')
    st.text(f'Gender: {gender_category}')
    st.text(f'Hobby:{",".join(hobby)}')


'''
st.code(code,language='python')