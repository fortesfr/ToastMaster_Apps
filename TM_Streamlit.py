#Streamlit App
import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api.formatters import JSONFormatter
# import json
from transcriber import youtube_transcripter


st.write("TestHiMeow")

moo = st.text_input(label, value="YouTube Url", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False)
st.write(moo)
# texter = st.file_uploader("Upload Me", type ='txt')
video_id = "oGb2oXZzIwY"
texter = youtube_transcripter(video_id)
# text = texter.read()

st.write(texter)
