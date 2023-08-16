def download(link, path):
    import os
    import youtube_dl as yt
    from android.os import Environment
    path = str(Environment.getExternalStorageDirectory()) + "/Download/ytdl/%(title)s.%(ext)s"

    ydl_opts = {
        "outtmpl": path,
        "format": '137+bestaudio/best',
        "ignoreerrors": True,
        "cachedir": False,

    }
    with yt.YoutubeDL(ydl_opts) as ydl:
       # info_dict = ydl.extract_info(link, download=False)
       # video_title = str(info_dict.get('title', None))
        ydl.download([link])
        #return video_title


def convertToAudio(link, path):
    from com.arthenica.mobileffmpeg import FFmpeg
    import subprocess


   # title = download(link, path)
    subprocess.run("ffmpeg -i "+path+"/"+"Shortest Video on Youtube"+".mp4"+" "+"Shortest Video on Youtube"+".mp3",shell=True)

