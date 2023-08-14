from pytube import YouTube
from moviepy.editor import *

def download(link, path):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(path)
    except:
        print("An error has occurred")

def convertToAudio(path):
    video = VideoFileClip(path)
    video.audio.write_audiofile(path)

