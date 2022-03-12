#Streamlit App

import streamlit as st
from transcriber import youtube_transcripter


st.write("TestHiMeow")

# texter = st.file_uploader("Upload Me", type ='txt')

texter = youtube_transcripter("GVsUOuSjvcg")
text = texter.read()

st.write(text)