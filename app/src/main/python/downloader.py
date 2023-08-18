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
    # return video_title


def convertToAudio(link, path):
    from com.arthenica.mobileffmpeg import FFmpeg
    from android.os import Environment
    # title = download(link, path)
    FFmpeg.execute("-i " + str(
        Environment.getExternalStorageDirectory()) + "/Download/ytdl/Shrt.mp4" + " -vn -acodec libmp3lame -q:a 0 " + str(
        Environment.getExternalStorageDirectory()) + "Sh.mp3")
    print(str(
        Environment.getExternalStorageDirectory()) + "/Download/ytdl/%(title)s.%(ext)s")