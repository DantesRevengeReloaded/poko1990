import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import os
from pytube import YouTube
from pytube import Playlist
import webbrowser

root = tk.Tk()
root.title('Poko 1990 the ultimate YouTube downloader',)
root.geometry('400x680+300+100')
root.configure(bg='#8C001A')
root.minsize(width='400', height='650')

photo = PhotoImage(file = "prussia.png")
root.iconphoto(False, photo)

message = tk.Label(root, text='Welcome to the best YouTube downloader of West Attica', bg='#8C001A', fg='white')
message.place(rely='0.01')

message1 = tk.Label(root, text="Choose an option to start download", font= 'HELVETICA', bg='#8C001A', fg='white')
message1.place(rely='0.3')

message2 = tk.Label(root, text="Powered by Pokomaster\n The True Master of Poko\n copyright 2023\n All Rights Reserved", bg='#8C001A', fg='white')
message2.place(rely='0.8')

destination = 'C:\\Users\\User\\Music\\YouTube Music'

def yturl() :
    webbrowser.open('https://www.youtube.com')

ytbutton=tk.Button(root, text = 'Click to open YouTube', command=yturl, font='HELVETICA', bg='#8C001A', fg='white', borderwidth='5')
ytbutton.place (rely='0.1')

def getdata() :
    global ytlink2
    ytlink2= ytlink.get()
    singledl()

def singlelink() :
    global windlink
    windlink = Toplevel()
    windlink.title('Download and convert a single video')
    windlink.geometry('500x200')
    messagewindlink = tk.Label(windlink, text = 'Please enter a proper YouTube link: ')
    messagewindlink.pack()
    global ytlink
    ytlink = Entry(windlink, width=50)
    ytlink.pack()
    singledlbutton = Button(windlink, text = 'Download and convert video to mp3', command=getdata)
    singledlbutton.pack()

def singledl():
    try :
        yt = YouTube(ytlink2)
        video = yt.streams.filter(only_audio=True).first()
        dlfile = video.download(destination)
        base, ext = os.path.splitext(dlfile)
        new_file = base + '.mp3'
        os.rename(dlfile, new_file)
        global goodmess
        goodmess = tk.Label(windlink, text= 'video: ' + yt.title + ' was downloaded successfully!')
        goodmess.pack()
    except :
        global badmess
        badmess = tk.Label(windlink, text= 'Oops an error occurred, check url or connection')
        badmess.pack()

def opentextlist() :
    global listofsongs
    windlink1.filename = filedialog.askopenfilename()
    listofsongs=windlink1.filename
    listofsongs=open(listofsongs)
    for line in listofsongs:
        line.split()
        line = line.strip()
        link = line
        yt = YouTube(link)
        video = yt.streams.filter(only_audio=True).first()
        try:
            dlfile = video.download(destination)
            base, ext = os.path.splitext(dlfile)
            new_file = base + '.mp3'
            os.rename(dlfile, new_file)
            print ('the file with name --',yt.title,'-- was downloaded successfully')
            messagewindlink2 = tk.Label(windlink1, text= 'video: ' + yt.title + ' was downloaded successfully!', font='HELVETICA', bg='black', fg='white')
            messagewindlink2.pack()
        except:
            print ('error has occurred, file with the following url wasnt downloaded:',yt)
            messagewindlink3 = tk.Label(windlink1, text='An error Has occurred, a file wasnt downloaded',font='HELVETICA')
            messagewindlink3.pack()

def listlink() :
    global windlink1
    windlink1 = Toplevel()
    windlink1.title('Download and convert videos from txt list')
    windlink1.geometry('600x200')
    windlink1.configure(bg='black')
    global buttonlist
    buttonlist = tk.Button(windlink1, text = 'Browse a text list And Download', bg='red', fg='white', font='HELVETICA', command=opentextlist)
    buttonlist.pack()

def playlistlink() :
    global windlink2
    windlink2 = Toplevel()
    windlink2.title('Download and convert videos from YouTube Playlist')
    windlink2.geometry('600x200')
    windlink2.configure(bg='brown')
    message4 =tk.Label(windlink2, text='Please enter a playlist url: ')
    message4.pack()
    global entryplaylist
    entryplaylist = tk.Entry(windlink2, width=50)
    entryplaylist.pack()
    global buttonplaylist
    buttonplaylist = tk.Button(windlink2, text='Download and convert all videos from playlist', font='HELVETICA', bg='green', command=getdata2)
    buttonplaylist.pack()

def getdata2() :
    global ytplaylistlink
    ytplaylistlink = entryplaylist.get()
    playlistdl()

def playlistdl() :
    global ytlist
    ytlist = Playlist(ytplaylistlink)
    for sololink in ytlist :
        videourl = YouTube(sololink)
        video = videourl.streams.filter(only_audio=True).first()
        try:
            dlfile2 = video.download(destination)
            base, ext = os.path.splitext(dlfile2)
            new_file = base + '.mp3'
            os.rename(dlfile2, new_file)
            print ('the file with name --',videourl.title,'-- was downloaded successfully')
            messagewindlink2 = tk.Label(windlink2, text= 'video: ' + videourl.title + ' was downloaded successfully!', font='HELVETICA', bg='brown', fg='white')
            messagewindlink2.pack()
        except:
            print ('error has occurred, file with the following url wasnt downloaded:',videourl)
            messagewindlink4 = tk.Label(windlink2, text='An error Has occurred, a file wasnt downloaded', font='HELVETICA')
            messagewindlink4.pack()

choosebutton1 = tk.Button(root, text='Single Download (paste link)', font='HELVETICA', width=30, bg='blue', command=singlelink).place(rely='0.4')
choosebutton2 = tk.Button(root, text='Download From *.txt list', font='HELVETICA', width=30, bg='blue', command=listlink).place(rely='0.5')
choosebutton3 = tk.Button(root, text='Download YouTube Playlist', font='HELVETICA', width=30, bg='blue', command=playlistlink).place(rely='0.6')

root.mainloop()