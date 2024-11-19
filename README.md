# simpleYT2mov
<<<<<<< HEAD
Simple YouTube App that will download a YouTube Video for you locally as a mp4 file. The files will be saved in a dictory called videos in the root directory.

Available switches for options:
--transcribe yes/no #This allows you for transcribing the downloaded video and transcribing the video- this will require the installation of the whisper library. The default is no.
--url <youtube-video-url> #this is the video url from YouTube for the videoy you wish to download.
--quality #default is the highest available resolution but you can adjust with another resolution if desired.

Sample Syntax:
python main.py --transcribe yes --url https://www.youtube.com/watch?v=zdQUdf23Lag

################################
This script has practical usability in extracting Youtube video into text for RAG systems. The text can easily be loaded into a document loader, node parser, and index for RAG retrievals.
With slight adjustments, this could be triggered as script or even executed via a streamlit application.
=======
Simple YouTube App that will download a YouTube Video for you locally as a mp4 file. 

#update:
The app now takes a list of YouTube Video and downloads each one with a 5 sec pause in between. The logic 
has been implemented to ensure each video is only downloaded once if you have a large list with duplication.

Added functionality to take an optional txt list file if you have a large of list of movies to download.
Usage: python3 main.py --file <list.txt>
