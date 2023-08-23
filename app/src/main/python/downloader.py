class Downloader:
    def __init__(self):
        self.file = []
        self.progress_bar = None

    def hook(self, downloading):
        if downloading["status"] == "finished":
            self.file.append(downloading["filename"])
        if downloading["status"] == "downloading":
            self.current_statement(downloading["percentage"])
            pass

    def current_statement(self, progress):
        self.progress_bar.setProgress(progress)

    def download(self, link):
        import os
        import youtube_dl as yt
        from android.os import Environment
        from com.arthenica.mobileffmpeg import FFmpeg

        path = str(Environment.getExternalStorageDirectory()) + f'/Download/ytdl/video.%(ext)s'
        yt_opts = {
            "outtmpl": path,
            "format": '137+bestaudio/best',
            "ignoreerrors": True,
            "cachedir": False,
            "progress_hooks": [self.hook]
        }
        yt.YoutubeDL(yt_opts).download([link])

        if len(self.file) == 2:
            folder = str(Environment.getExternalStorageDirectory()) + "/Download/ytdl/"
            last_name = folder + f"vid.mp4"

            FFmpeg.execute("-i " + self.file[0] + " -i " + self.file[
                1] + " -c:v copy -c:a aac " + last_name)
            self.file.append(last_name)
            os.remove(self.file[0])
            os.remove(self.file[1])

    def convertToAudio(self, link):
        import os
        from com.arthenica.mobileffmpeg import FFmpeg
        from android.os import Environment
        self.download(link)
        FFmpeg.execute("-i " + str(
            Environment.getExternalStorageDirectory()) + "/Download/ytdl/" + "video.mp4" + " -vn -acodec libmp3lame -q:a 0 " + str(
            Environment.getExternalStorageDirectory()) + "/Download/ytdl/" + "audio.mp3")
        os.remove(self.file[2])


def start(link, action, progress_bar):
    downloader = Downloader()
    downloader.progress_bar = progress_bar
    if action == "v" or action == "video":
        downloader.download(link)
    else:
        downloader.convertToAudio(link)
