#Streamlit App

import streamlit as st
from transcriber import youtube_transcripter
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import json


st.write("TestHiMeow")

# texter = st.file_uploader("Upload Me", type ='txt')

texter = youtube_transcripter("GVsUOuSjvcg")
text = texter.read()

st.write(text)