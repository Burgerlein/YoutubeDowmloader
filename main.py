from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    try:
        video = youtubeObject.streams.get_highest_resolution()
        video.download()

    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = str(input("Geben sie den Youtube Link ein: "))
Download(link)