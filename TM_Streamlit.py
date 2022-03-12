#Streamlit App

import streamlit as st

st.write("TestHiMeow")

texter = st.file_uploader("Upload Me", type ='txt')

text = texer.read()

st.write(text)