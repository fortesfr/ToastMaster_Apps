#Streamlit App

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import json
from transcriber import youtube_transcripter


st.write("TestHiMeow")

# texter = st.file_uploader("Upload Me", type ='txt')

text = youtube_transcripter("GVsUOuSjvcg")
# text = texter.read()

# st.write(text)