class Downloader:
    def __init__(self):
        self.file = []
        self.current_statement = 0

    def return_progress_statement(self):
        return self.current_statement

    def hook(self, downloading):
        if downloading["status"] == "finished":
            self.file.append(downloading["filename"])
        if downloading["status"] == "downloading":
            self.current_statement = int(downloading["downloaded_bytes"] / downloading["total_bytes_estimate"] * 100)


    def download(self, link):
        import os
        import youtube_dl as yt
        from android.os import Environment
        from java.io import File
        from com.arthenica.mobileffmpeg import FFmpeg

        path = str(
            File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS),
                 "file.%(ext)s"))
        yt_opts = {
            "outtmpl": path,
            "format": '137+bestaudio/best',
            "ignoreerrors": True,
            "cachedir": False,
            "progress_hooks": [self.hook]
        }
        yt.YoutubeDL(yt_opts).download([link])

        if len(self.file) == 2:
            folder = str(
                Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS))
            last_name = folder + f"/file.mp4"

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
            Environment.getExternalStoragePublicDirectory(
                Environment.DIRECTORY_DOWNLOADS)) + "/file.mp4" + " -vn -acodec libmp3lame -q:a 0 " + str(
            Environment.getExternalStoragePublicDirectory(
                Environment.DIRECTORY_DOWNLOADS)) + "/audio.mp3")
        os.remove(self.file[2])


downloader = Downloader()

def r():
    return downloader.current_statement
def start(link, action):
    if action == "v" or action == "video":
        downloader.download(link)
    else:
        downloader.convertToAudio(link)

