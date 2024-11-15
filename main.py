import os
import sys
import argparse
from yt_dlp import YoutubeDL
import whisper   #uncomment to use transcription

SAVE_DIR = "videos"
DEFAULT_URL = 'https://www.youtube.com/watch?v=CKr0soIf4jA'

def get_youtube_dl_options(quality):
    if quality:
        format_option = f"mp4[height={quality}]"
    else:
        format_option = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best'

    return {
        'format': format_option,
        "outtmpl": os.path.join(SAVE_DIR, "%(title)s-%(id)s.%(ext)s"),
        "restrictfilenames": True,
        "nooverwrites": True,
        "writedescription": False,
        "writeinfojson": False,
        "writeannotations": False,
        "writethumbnail": False,
        "writesubtitles": False,
        "writeautomaticsub": False
    }

def transcribe_video(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    transcript_path = os.path.splitext(video_path)[0] + ".txt"
    with open(transcript_path, "w") as f:
        f.write(result["text"])
    print(f"Transcription saved to {transcript_path}")

def clean_directory(directory):
    for filename in os.listdir(directory):
        if not (filename.endswith(".mp4") or filename.endswith(".txt")):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

def download(urls, quality, transcribe):
    youtube_dl_options = get_youtube_dl_options(quality)
    with YoutubeDL(youtube_dl_options) as ydl:
        ydl.download(urls)

    if transcribe:
        for url in urls:
            video_id = url.split("v=")[-1]
            # Find the correct video file based on the download pattern
            for filename in os.listdir(SAVE_DIR):
                if video_id in filename and filename.endswith(".mp4"):
                    video_path = os.path.join(SAVE_DIR, filename)
                    transcribe_video(video_path)
                    break

    clean_directory(SAVE_DIR)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos with specified quality and optional transcription.")
    parser.add_argument('--quality', type=str, help='Resolution of the video (e.g., 1080, 720).')
    parser.add_argument('--url', type=str, help='YouTube URL to download.')
    parser.add_argument('--transcribe', type=str, choices=['yes', 'no'], default='no', help='Transcribe the video (yes or no).')
    args = parser.parse_args()

    urls = [args.url] if args.url else [DEFAULT_URL]
    transcribe = args.transcribe.lower() == 'yes'
    download(urls, args.quality, transcribe)