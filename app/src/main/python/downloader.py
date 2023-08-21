class Downloader:
    def __init__(self):
        self.file = []

    def hook(self, downloading):
        if downloading["status"] == "finished":
            self.file.append(downloading["filename"])
        if downloading["status"] == "downloading":
            pass

    def download(self, link):
        import os
        import youtube_dl as yt
        from android.os import Environment
        from com.arthenica.mobileffmpeg import FFmpeg

        path = str(Environment.getExternalStorageDirectory()) + "/Download/ytdl/%(title)s.%(ext)s"

        ydl_opts = {
            "outtmpl": path,
            "format": '137+bestaudio/best',
            "ignoreerrors": True,
            "cachedir": False,
            "progress_hooks": [self.hook]

        }
        with yt.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            video_title = str(info_dict.get('title', None)).replace(" ", "_")# NOTICE FOR READERS: ffmpeg cannot work with files where spaces in a filename
            ydl.download([link])
            print(video_title)
            if len(self.file) == 2:
                folder = str(Environment.getExternalStorageDirectory()) + "/Download/ytdl/"
                last_name = folder + video_title + ".mp4"
                print(last_name)
                print(self.file[0])
                print(self.file[1])
                FFmpeg.execute("-i " + self.file[0] + " -i " + self.file[
                    1] + " -c:v copy -c:a aac " + last_name)
                os.remove(self.file[0])
                os.remove(self.file[1])
            return video_title

    def convertToAudio(self, link):
        from com.arthenica.mobileffmpeg import FFmpeg
        from android.os import Environment
        title = self.download(link)
        FFmpeg.execute("-i " + str(
            Environment.getExternalStorageDirectory()) + "/Download/ytdl/" + title + ".mp4" + " -vn -acodec libmp3lame -q:a 0 " + str(
            Environment.getExternalStorageDirectory()) + "/Download/ytdl/" + title + ".mp3")


def start(link, action):
    downloader = Downloader()
    if action == "v" or action == "video":
        downloader.download(link)
    else:
        downloader.convertToAudio(link)

class Downloader:
    def __init__(self):
        self.file = []

    def hook(self, downloading):
        if downloading["status"] == "finished":
            self.file.append(downloading["filename"])
        if downloading["status"] == "downloading":
            pass

    def download(self, link):
        import os
        import youtube_dl as yt
        from android.os import Environment
        from com.arthenica.mobileffmpeg import FFmpeg

        path = str(Environment.getExternalStorageDirectory()) + "/Download/ytdl/%(title)s.%(ext)s"

        ydl_opts = {
            "outtmpl": path,
            "format": '137+bestaudio/best',
            "ignoreerrors": True,
            "cachedir": False,
            "progress_hooks": [self.hook]

        }
        with yt.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            video_title = str(info_dict.get('title', None)).replace(" ", "_")# NOTICE FOR READERS: ffmpeg cannot work with files where spaces in a filename
            ydl.download([link])
            print(video_title)
            if len(self.file) == 2:
                folder = str(Environment.getExternalStorageDirectory()) + "/Download/ytdl/"
                last_name = folder + video_title + ".mp4"
                print(last_name)
                print(self.file[0])
                print(self.file[1])
                FFmpeg.execute("-i " + self.file[0] + " -i " + self.file[
                    1] + " -c:v copy -c:a aac " + last_name)
                os.remove(self.file[0])
                os.remove(self.file[1])
            return video_title

    def convertToAudio(self, link):
        from com.arthenica.mobileffmpeg import FFmpeg
        from android.os import Environment
        title = self.download(link)
        FFmpeg.execute("-i " + str(
            Environment.getExternalStorageDirectory()) + "/Download/ytdl/" + title + ".mp4" + " -vn -acodec libmp3lame -q:a 0 " + str(
            Environment.getExternalStorageDirectory()) + "/Download/ytdl/" + title + ".mp3")


def start(link, action):
    downloader = Downloader()
    if action == "v" or action == "video":
        downloader.download(link)
    else:
        downloader.convertToAudio(link)

