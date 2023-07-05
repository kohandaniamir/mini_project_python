from tkinter import *

root = Tk()
root.title("Number puzzle")

root.geometry(f"{458}x{600}+{500}+{130}")
root.resizable(False,False)
background_color = "gray"
root.config(bg=background_color)


btn_1 = Button(root,text="1",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_1.place(x=2,y=2)

btn_2 = Button(root,text="2",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_2.place(x=116,y=2)

btn_3 = Button(root,text="3",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_3.place(x=230,y=2)

btn_4 = Button(root,text="4",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_4.place(x=344,y=2)

btn_5 = Button(root,text="5",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_5.place(x=2,y=131)


btn_6 = Button(root,text="6",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_6.place(x=116,y=131)

btn_7 = Button(root,text="7",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_7.place(x=230,y=131)

btn_8 = Button(root,text="8",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_8.place(x=344,y=131)

btn_9 = Button(root,text="9",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_9.place(x=2,y=260)

btn_10 = Button(root,text="10",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_10.place(x=116,y=260)

btn_11 = Button(root,text="11",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_11.place(x=230,y=260)

btn_12 = Button(root,text="12",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_12.place(x=344,y=260)

btn_13 = Button(root,text="13",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_13.place(x=2,y=390)

btn_14 = Button(root,text="14",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_14.place(x=116,y=390)

btn_15 = Button(root,text="15",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_15.place(x=230,y=390)

btn_16 = Button(root,text="",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5")
btn_16.place(x=344,y=390)


btn_down = Button(root,text="check",bd=1,bg="gray",fg="white",width=20,height=3,activebackground="#1B6AA5")
btn_down.place(x=155,y=525)


root.mainloop()