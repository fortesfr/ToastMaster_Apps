#Streamlit App
import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api.formatters import JSONFormatter
# import json
from transcriber import youtube_transcripter


st.header("Download Transcripts from Videos")

moo = st.text_input('Input', value="YouTube Url")
st.write(moo)
# texter = st.file_uploader("Upload Me", type ='txt')
video_id = "oGb2oXZzIwY"
texter = youtube_transcripter(video_id)
# text = texter.read()

st.write(texter)
