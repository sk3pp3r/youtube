import sys
from youtube_transcript_api import YouTubeTranscriptApi

# Optional video_id variable
default_video_id = "pxiP-HJLCx0"

def print_transcript(video_id):
    srt = YouTubeTranscriptApi.get_transcript(video_id)
    
    for i in srt:
        print(i['text'])  # Print to screen

if __name__ == "__main__":
    video_id = default_video_id
    if len(sys.argv) == 2:
        video_id = sys.argv[1]
    elif len(sys.argv) > 2:
        print("Usage: python app.py [<video_id>]")
        sys.exit(1)
    
    print_transcript(video_id)
