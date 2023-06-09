from tkinter import *
# import pygame as pg

root = Tk()
root.title("music-player")                  #title of root
root.geometry("600x400")                    #select the size
root.resizable(width=False,height=False)    #fixed the size


#song track

trackFrame = LabelFrame(root,text="Song Track", bg="black",fg="white",font=("Arial",10),bd=5,relief=GROOVE)
trackFrame.place(x=10,y=10, width=580,height=100)

showsongname = Text(trackFrame,bg="white",fg="red",width=50,height=1,state=DISABLED)   # name song
showsongname.grid(row=0,column=0,padx=10,pady=20)

showstatus = Label(trackFrame,bg="white",fg="black",width=15)
showstatus.grid(row=0,column=1,padx=20)

#control panel

cpanel = LabelFrame(root,text="Control Panel", bg="black",fg="white",font=("Arial",10),bd=5,relief=GROOVE,padx=15)
cpanel.place(x=10,y=120, width=580,height=100)

play = Button(cpanel,text="play",width=15)
play.grid(row=0,column=0,padx=10,pady=20)

stop = Button(cpanel,text="stop",width=15)
stop.grid(row=0,column=1,padx=10,pady=20)

unpausing = Button(cpanel,text="unpausing",width=15)
unpausing.grid(row=0,column=2,padx=10,pady=20)

pausing = Button(cpanel,text="pausing",width=15)
pausing.grid(row=0,column=3,padx=10,pady=20)

root.mainloop()









root.mainloop()