import youtube_dl as yt


def download(link, path):
    import os
    import youtube_dl as yt
    from android.os import Environment
    path = str(Environment.getExternalStorageDirectory()) +"/Download/ytdl/%(title)s.%(ext)s"

    ydl_opts = {
        "outtmpl": path,
        "format": '137+bestaudio/best',
        "ignoreerrors": True,
        "cachedir": False,

    }
    with yt.YoutubeDL(ydl_opts) as ydl:
      #  info_dict = ydl.extract_info(link, download=True)
      #  video_title = str(info_dict.get('title', None))
        ydl.download([link])

        return "Done Downloading"


def convertToAudio(path):
    from com.arthenica.mobileffmpeg import FFmpeg
    video = VideoFileClip(path)
    video.audio.write_audiofile(path)
