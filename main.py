from pytube import YouTube
from pick import pick

title = 'Please Choose an option where to install the video: '
options = ['Desktop', 'Dowmloads Folder']
option, index = pick(options, title, indicator='=>', default_index=0)

link = input("Geben sie den Youtube Link ein: ")