from tkinter import *
from pytube import YouTube

# base for GUI
base = Tk()
base.geometry("400x175")
base.title("Downloader")

def load():
    # function only allows download if link is valid
    try:
        myVar.set("Downloading...")
        base.update()
        vid = YouTube(link.get()).streams.get_highest_resolution()
        vid.download()
        link.set("Download successful")
    except Exception as e:
        myVar.set("Download Error")
        base.update()
        link.set("Enter correct link")

# generate the input boxes, text on GUI
Label(base, text="YouTube Downloader", font="SFPro 15 bold").pack()
myVar = StringVar()
myVar.set("Enter link below")
Entry(base, textvariable=myVar, width=35).pack(pady=10)
link = StringVar()
Entry(base, textvariable=link, width=35).pack(pady=10)
Button(base, text="Download", command=load).pack()
base.mainloop()

