from pytube import YouTube
link = input("Enter an URL: ")
youtube = YouTube(link)
videos = youtube.streams.all()

i=1
for stream in videos:
    print(str(i)+ " "+ str(stream))
    i+=1
stream_number= int(input("Enter a number to download from above:" ))
video = videos[stream_number-1]
video.download() # path, where to video download.
print("Successfully Downoaded.")