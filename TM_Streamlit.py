#Streamlit App
import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api.formatters import JSONFormatter
# import json
from transcriber import youtube_transcripter


st.header("Download Transcripts from Videos")

moo = st.text_input(' ', value="YouTube Url")

# video_id = "oGb2oXZzIwY"
# texter = youtube_transcripter(video_id)
# st.write(moo)

if st.button('Go'):
  texter = youtube_transcripter(moo)
  st.write(texter)
  
# texter = st.file_uploader("Upload Me", type ='txt')

# text = texter.read()

# st.write(texter)
