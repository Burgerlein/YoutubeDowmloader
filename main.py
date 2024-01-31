from pytube import YouTube
from pick import pick

title = 'Please Choose an option where to install the video: '
options = ['Desktop', 'Dowmloads Folder']
option, index = pick(options, title, indicator='=>', default_index=0)

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