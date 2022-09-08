
#importing hashlib
import hashlib
#importing tkinter
from tkinter import *
#importing youtube module
from pytube import YouTube
#initializing tkinter
root = Tk()
#setting the geometry of the GUI
root.geometry("600x350")
root.configure(background="white")
#setting the title of the GUI
root.title("YouTube VIDEO Downloader Application")
photo = PhotoImage(file = "icon.ico")
root.iconphoto(False, photo) 

#declaring StringVar type variable
link = StringVar()
link = str(link.get()).encode()
sha256 = hashlib.sha256(link)
estr = sha256.hexdigest()


#defining download functions
def nowdownload():
    try:
        youtube = YouTube(link)
        video = youtube.streams.first()
        video.download() # path, where to video download.
        myVar.set("Downloading...")
        root.update()
        msg.set("VIDEO DOWNLOADED SUCCESFULLY.")
    except Exception as e:
        myVar.set("An error occured!!")
        root.update()
        msg.set("Enter correct link")

#create the label widget to welcome user
Label(root, text = "WELCOME USER!\nYouTube VIDEOS Downloader Application", font = "Helvetica 15 bold", background="white").pack()
#declaring StringVar type variable
myVar = StringVar()
#declaring StringVar type variable
msg = StringVar()
#adding image
myImage = PhotoImage(file = "logo.png")
pic = Label(root, image = myImage).pack()
#setting the deafult text to my Var
myVar.set("Enter the Link below")
#created the enty widgetfor user to enter URL
Label(root, textvariable = myVar,  font = "times 12 bold", background="white").pack()
#created the enty widget to enter link
Entry(root, textvariable = link, width=40,background="white").pack(pady= 10)
#created and called the download function
#created the enty widgetfor user to enter URL
Label(root, textvariable = msg,  font = "times 11 bold", background="white").pack()
Button(root, text ="Start Download", font = "helvetica 8 bold", command = nowdownload, background="red").pack()
#running the main loop
root.mainloop()

