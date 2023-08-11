from pytube import YouTube

def download(link, path):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    try:
        youtubeObject.download(path)
    except:
        print("An error has occurred")
    print("Download is completed successfully")
