#Streamlit App

import streamlit as st

st.write("TestHiMeow")

text = st.file_uploader("Upload Me", type ='txt')

st.write(text)