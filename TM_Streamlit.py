#Streamlit App
import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api.formatters import JSONFormatter
# import json
from transcriber import youtube_transcripter


st.header("Download Transcripts from Videos")

url_input = st.text_input(' ', value="YouTube Url")
if url_input:
  texter = youtube_transcripter(url_input)
  st.write(texter)
  

# video_id = "oGb2oXZzIwY"
# texter = youtube_transcripter(video_id)
# st.write(moo)

if st.button('Go'):
  texter = youtube_transcripter(url_input)
  st.write(texter)
  
# texter = st.file_uploader("Upload Me", type ='txt')

# text = texter.read()

# st.write(texter)
