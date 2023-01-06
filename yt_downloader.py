from tkinter import *
from pytube import YouTube
import os

# base for GUI
base = Tk()
base.geometry("400x225")
base.title("Downloader")


def loadmp3():
    # downloads video in .mp3 format
    # function only allows download if link is valid
    try:
        myVar.set("Downloading...")
        base.update()
        vid = YouTube(link.get()).streams.filter(only_audio=True).first()
        file_out = vid.download()
        name, ext = os.path.splitext(file_out)
        file_rename = name + ".mp3"
        os.rename(file_out, file_rename)
        myVar.set("Download successful")
    except Exception as e:
        myVar.set("Download Error")
        base.update()
        link.set("Enter correct link")


def loadmp4():
    # downloads video in .mp4 format
    try:
        myVar.set("Downloading...")
        base.update()
        vid = YouTube(link.get()).streams.get_highest_resolution()
        vid.download()
        myVar.set("Download successful")
    except Exception as e:
        myVar.set("Download Error")
        base.update()
        link.set("Enter correct link")


# generate the input box, text on GUI
my_font = "SFPro 15 bold"
Label(base, text="YouTube Downloader", font=my_font).pack()
myVar = StringVar()
myVar.set("Enter link below")
Label(base, textvariable=myVar, font=my_font).pack(pady=5)
link = StringVar()
Entry(base, textvariable=link, width=35).pack(pady=7)
Button(base, text="Download as .mp3", command=loadmp3).pack(pady=10)
Button(base, text="Download as .mp4", command=loadmp4).pack(pady=7)

base.mainloop()
