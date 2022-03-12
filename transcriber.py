
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import json

video_id = "GVsUOuSjvcg"

def youtube_transcripter(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = JSONFormatter()
    json_formatted = formatter.format_transcript(transcript)

    with open('your_filename.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_formatted)

    file = json_formatted.replace('\\n', ' ')
    text_raw = json.loads(file)
    return text_raw
