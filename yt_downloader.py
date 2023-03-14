from tkinter import *
from pytube import YouTube
import os

# base for GUI
base = Tk()
base.geometry("400x300")
base.title("Downloader")


def check_directory():
    # checks if directory link inputted in text box
    if not dir.get():
        return False
    else:
        return True


def convert_mp3(file_out):
    # converts download to .mp3
    name, ext = os.path.splitext(file_out)
    file_rename = name + ".mp3"
    os.rename(file_out, file_rename)


def loadmp3():
    # downloads video in .mp3 format
    # function only allows download if link is valid
    try:
        myVar.set("Downloading...")
        base.update()
        vid = YouTube(link.get()).streams.filter(only_audio=True).first()
        dircheck = check_directory()
        if not dircheck:
            file_out = vid.download()
            convert_mp3(file_out)
        else:
            file_out = vid.download(dir.get())
            convert_mp3(file_out)
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
        dircheck = check_directory()
        if not dircheck:
            vid.download()
        else:
            vid.download(dir.get())
        myVar.set("Download successful")
    except Exception as e:
        myVar.set("Download Error")
        base.update()
        link.set("Enter correct link")


# generate input box, text on GUI
my_font = "SFPro 15 bold"
Label(base, text="YouTube Downloader", font=my_font).pack()

# entry box for video link
myVar = StringVar()
myVar.set("Enter link below")
Label(base, textvariable=myVar, font=my_font).pack(pady=5)
link = StringVar()
Entry(base, textvariable=link, width=35).pack(pady=7)

# entry box for directory link
dir_label = StringVar()
dir_label.set("(Optional) Enter directory")
Label(base, textvariable=dir_label, font=my_font).pack(pady=7)
dir = StringVar()
Entry(base, textvariable=dir, width=35).pack(pady=7)

# buttons to initiate download
Button(base, text="Download as .mp3", command=loadmp3).pack(pady=10)
Button(base, text="Download as .mp4", command=loadmp4).pack(pady=7)

base.mainloop()
