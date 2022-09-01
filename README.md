<h2># Research</h2>
<p>I found that python is a powerful language. According to my research, it can be used for Machine Learning, Deep Learning and using Internet things, etc.
Including this, I am specifically interested in There are three Frame Work which allows for making web site easier.</p>
<ul>
    <li>-Django</li>
    <li>-Flask</li>
    <li>-Streamlit</li>
</ul>

<p>I am looking at all frameworks I discovered that streamlit was super easy to deploy content on a server.
And only use python code.
like that
I dployed on this space for free using github.</p>

<a href="https://20220920-research--main-app-j8pl0v.streamlitapp.com/">this is a link 'https://20220920-research--main-app-j8pl0v.streamlitapp.com'</a>

<p>All code was
Folder Name.</p>
<h2>-main_app.py code</h2>

<p>st.title('Kentaro App')</p> #title very easy and we do not use HTML

<p>st.caption('This is my research')</p>


<p>col1, col2 =st.columns(2) #separate 
with col1:</p>

<p>image =Image.open ('./data/IMG_2026.JPG') #Add Picture
 st.image(image,width=350)</p>
<p> st.subheader('Introduction')</p>
 <p>st.text('My name is Kentaro Kamiya.')
 st.text('I have been living in New Zealand 
'
         'since 2011.I live here with my family')</p>
 <p>video_file= open('./data/ISYQ5032.mov','rb') #Add Movie
 video_bytes=video_file.read()
 st.video(video_bytes)</p>

<p>with col2:
 st.subheader('This is my sons')
 </p>
 
 <h2>-Page_1.py Code</h2>

<p>st.title('Widget')</p>

<p>with st.form(key='profile_form'):<br>
 name= st.text_input('Name')</p>

 <p>gender_category=st.radio(
     'Gender',
     ('Man','Woman')
 )</p>
<p> hobby=st.multiselect(
     'Hobby',
     ('Sport','Anime','Movie','Fishing','Cooking','etc')
 )</p>
 
 <p>height=st.slider('Height',min_value=110, max_value=210)</p>

<p> submit_btn= st.form_submit_button('Send')
 cancel_btn= st.form_submit_button('Cancel')</p>
 <p>if submit_btn:<br>
    st.text(f'Hello!{name}')<br>
    st.text(f'Gender: {gender_category}')<br>
    st.text(f'Hobby:{",".join(hobby)}')</p>
 <h2>code that you've been inspired by (with comments)</h2>
  <p>height=st.slider('Height',min_value=110, max_value=210)</p>
     #Only this code can make sider without any function.
  <p>hobby=st.multiselect(
     'Hobby',
     ('Sport','Anime','Movie','Fishing','Cooking','etc')</P>  
     #I can easy to insert multiselect widget on my website
 <h2>Conclusion</h2>
 <p>Streamlit can make web site just using python code.
 And very easy to create any web application.</p>
<p> I tried graphs about stock prices or inserting any scientific data but 
 it too hard to show in this research<br> otherefore I have to keep learning
 basics of python language.</p>
<p>Anyway, Streamlit framework can make creating web site easier<br> as well as even more become powerful.</p>
