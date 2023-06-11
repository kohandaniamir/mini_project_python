from tkinter import *
import pygame as pg
import os
from pygame import mixer
pg.init()
pg.mixer.init()

root = Tk()
root.title("music-player")                  #title of root
root.geometry("600x400")                    #select the size
root.resizable(width=False,height=False)    #fixed the size

status=StringVar()

# ======================button=========================
def playsong():
    showsongname.config(state=NORMAL)
    showsongname.delete("1.0",END)
    showsongname.insert("1.0",playlist.get(ACTIVE))
    showsongname.config(state=DISABLED)
    status.set("Playing")
    pg.mixer.music.load(playlist.get(ACTIVE))
    pg.mixer.music.play()

def stopsong():
    showsongname.config(state=NORMAL)
    showsongname.delete("1.0", END)
    showsongname.config(state=DISABLED)
    pg.mixer.music.stop()
    status.set("Stopped")


def unpausingsong():
    pg.mixer.music.unpause()
    status.set("Playing")

def pausingsong():
    pg.mixer.music.pause()
    status.set("Paused")

#================= play list=====================

songFrame = LabelFrame(root,text="Song play list", bg="black",fg="white",font=("Arial",10),bd=5,relief=GROOVE)
songFrame.place(x=10,y=1, width=580,height=210)

scroll =Scrollbar(songFrame,orient=VERTICAL)

playlist=Listbox(songFrame,bg="silver",fg="black",relief=GROOVE,font=("Arial",10),selectmode=SINGLE,selectbackground="black",height=100
                 ,yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(fill=BOTH)
#==============song track=====================

trackFrame = LabelFrame(root,text="Song Track", bg="black",fg="white",font=("Arial",10),bd=5,relief=GROOVE)
trackFrame.place(x=10,y=210, width=580,height=90)

showsongname = Text(trackFrame,bg="white",fg="red",width=50,height=1,state=DISABLED)   # name song
showsongname.grid(row=0,column=0,padx=10,pady=20)

showstatus = Label(trackFrame,bg="white",fg="black",width=15,textvariable=status)
showstatus.grid(row=0,column=1,padx=20)

#========================control panel===========================

cpanel = LabelFrame(root,text="Control Panel", bg="black",fg="white",font=("Arial",10),bd=5,relief=GROOVE,padx=15)
cpanel.place(x=10,y=295, width=580,height=100)

play = Button(cpanel,text="play",width=15,command=lambda :playsong())
play.grid(row=0,column=0,padx=10,pady=20)

stop = Button(cpanel,text="stop",width=15,command=lambda:stopsong())
stop.grid(row=0,column=1,padx=10,pady=20)

unpausing = Button(cpanel,text="unpausing",width=15,command=lambda:unpausingsong() )
unpausing.grid(row=0,column=2,padx=10,pady=20)

pausing = Button(cpanel,text="pausing",width=15,command=lambda:pausingsong() )
pausing.grid(row=0,column=3,padx=10,pady=20)


os.chdir(r" ") #your music folder
mysong=os.listdir()

for song in mysong:
    if ".mp3" in song:
        playlist.insert(END,song)


root.mainloop()
