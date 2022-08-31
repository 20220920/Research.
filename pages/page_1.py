import streamlit as st
from PIL import Image

st.title('Widget')
with st.form(key='profile_form'):
 name= st.text_input('Name')
 
 gender_category=st.radio(
     'Gender',
     ('Male','Female')
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




