
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import json
import pandas as pd

video_id = "GVsUOuSjvcg"

def youtube_transcripter(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = JSONFormatter()
    json_formatted = formatter.format_transcript(transcript)

    with open('your_filename.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_formatted)

    file = json_formatted.replace('\\n', ' ')
    text_raw = json.loads(file)

    pd.set_option('display.max_colwidth', None)
    text_df = pd.DataFrame(text_raw)
    text = text_df['text']
    text_str = text.to_string(index=False)
    return text_str