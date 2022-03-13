#Streamlit App
import streamlit as st
# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api.formatters import JSONFormatter
# import json
from transcriber import youtube_transcripter


st.header("Download Transcripts from Videos")

url_input_raw = st.text_input(' ', value="https://www.youtube.com/watch?v=GVsUOuSjvcg")
# https://youtu.be/ER9FlyYr_QA


if url_input_raw:
  if search('www.youtube.com', url_input_raw):
    url_input = url_input_raw.replace('https://www.youtube.com/watch?v=', ''):
    # url_input = url_input_raw.str()
    # url_input = url_input.translate({ord(i): None for i in 'https://www.youtube.com/watch?v='})
    texter = youtube_transcripter(url_input)
   else: 
    input_url = url_input_raw.replace('https://youtu.be/', '')
    texter = youtube_transcripter(url_input)
  st.write(texter)
else:
  st.write("HI")
  
  

# video_id = "oGb2oXZzIwY"
# texter = youtube_transcripter(video_id)
# st.write(moo)

if st.button('Download'):
  st.write("DOwnloading!")
  
# texter = st.file_uploader("Upload Me", type ='txt')

# text = texter.read()

# st.write(texter)
