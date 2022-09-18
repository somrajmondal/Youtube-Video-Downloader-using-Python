from pytube import YouTube

link="https://www.youtube.com/watch?v=OFAY5QgjeNQ"
youtube_1= YouTube(link)
#print(youtube_1.title)
#print(youtube_1.thumbnail_url)
video=youtube_1.streams.all()  #all format
#video=youtube_1.streams.filter(only_audio=True)
vid=list(enumerate(video))
for i in vid:
    print(i)
print()
strm=int(input('Enter quality:'))
video[strm].download()
print('Download Completed')

# *******Playlist***
from pytube import Playlist
py=Playlist('https://www.youtube.com/playlist?list=PLjVLYmrlmjGcCGxsGGB6c0oPLvqQs-DAw')
print(f'Downloading: {py.title}')
for video in py.videos:
    video.streams.first().download()
