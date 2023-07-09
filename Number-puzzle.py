from tkinter import Tk,messagebox,Button
import random
root = Tk()
root.title("Number puzzle")

root.geometry(f"{458}x{600}+{500}+{130}")
root.resizable(False,False)
background_color = "gray"
root.config(bg=background_color)

def replace():
    number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    btns = [btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,btn_11,btn_12,btn_13,btn_14,btn_15]
    for i in btns:
        rand =random.choice(number)
        i.configure(text=rand)
        number.remove(rand)
def btn__():
    if btn_12["text"] == "":
        number = btn_["text"]
        btn_12.configure(text=number)
        btn_.configure(text="")
    elif btn_15["text"] == "":
        number = btn_["text"]
        btn_15.configure(text=number)
        btn_.configure(text="")


def btn15():
    if btn_["text"] == "":
        number = btn_15["text"]
        btn_.configure(text=number)
        btn_15.configure(text="")
    elif btn_11["text"] == "":
        number = btn_15["text"]
        btn_11.configure(text=number)
        btn_15.configure(text="")
    elif btn_14["text"] == "":
        number = btn_15["text"]
        btn_14.configure(text=number)
        btn_15.configure(text="")


def btn14():
    if btn_15["text"] == "":
        number = btn_14["text"]
        btn_15.configure(text=number)
        btn_14.configure(text="")
    elif btn_10["text"] == "":
        number = btn_14["text"]
        btn_10.configure(text=number)
        btn_14.configure(text="")
    elif btn_13["text"] == "":
        number = btn_14["text"]
        btn_13.configure(text=number)
        btn_14.configure(text="")

def btn13():
    if btn_14["text"] == "":
        number = btn_13["text"]
        btn_14.configure(text=number)
        btn_13.configure(text="")
    elif btn_9["text"] == "":
        number = btn_13["text"]
        btn_9.configure(text=number)
        btn_13.configure(text="")


def btn12():
    if btn_11["text"] == "":
        number = btn_12["text"]
        btn_11.configure(text=number)
        btn_12.configure(text="")
    elif btn_8["text"] == "":
        number = btn_12["text"]
        btn_8.configure(text=number)
        btn_12.configure(text="")
    elif btn_["text"] == "":
        number = btn_12["text"]
        btn_.configure(text=number)
        btn_12.configure(text="")

def btn11():
    if btn_12["text"] == "":
        number = btn_11["text"]
        btn_12.configure(text=number)
        btn_11.configure(text="")
    elif btn_7["text"] == "":
        number = btn_11["text"]
        btn_7.configure(text=number)
        btn_11.configure(text="")
    elif btn_10["text"] == "":
        number = btn_11["text"]
        btn_10.configure(text=number)
        btn_11.configure(text="")
    elif btn_15["text"] == "":
        number = btn_11["text"]
        btn_15.configure(text=number)
        btn_11.configure(text="")

def btn10():
    if btn_6["text"] == "":
        number = btn_10["text"]
        btn_6.configure(text=number)
        btn_10.configure(text="")
    elif btn_9["text"] == "":
        number = btn_10["text"]
        btn_9.configure(text=number)
        btn_10.configure(text="")
    elif btn_14["text"] == "":
        number = btn_10["text"]
        btn_14.configure(text=number)
        btn_10.configure(text="")
    elif btn_11["text"] == "":
        number = btn_10["text"]
        btn_11.configure(text=number)
        btn_10.configure(text="")



def btn9():
    if btn_5["text"] == "":
        number = btn_9["text"]
        btn_5.configure(text=number)
        btn_9.configure(text="")
    elif btn_10["text"] == "":
        number = btn_9["text"]
        btn_10.configure(text=number)
        btn_9.configure(text="")
    elif btn_13["text"] == "":
        number = btn_9["text"]
        btn_13.configure(text=number)
        btn_9.configure(text="")

def btn8():
    if btn_4["text"] == "":
        number = btn_8["text"]
        btn_4.configure(text=number)
        btn_8.configure(text="")
    elif btn_7["text"] == "":
        number = btn_8["text"]
        btn_7.configure(text=number)
        btn_8.configure(text="")
    elif btn_12["text"] == "":
        number = btn_8["text"]
        btn_12.configure(text=number)
        btn_8.configure(text="")

def btn7():
    if btn_3["text"] == "":
        number = btn_7["text"]
        btn_3.configure(text=number)
        btn_7.configure(text="")
    elif btn_6["text"] == "":
        number = btn_7["text"]
        btn_6.configure(text=number)
        btn_7.configure(text="")
    elif btn_8["text"] == "":
        number = btn_7["text"]
        btn_8.configure(text=number)
        btn_7.configure(text="")
    elif btn_11["text"] == "":
        number = btn_7["text"]
        btn_11.configure(text=number)
        btn_7.configure(text="")

def btn6():
    if btn_2["text"] == "":
        number = btn_6["text"]
        btn_2.configure(text=number)
        btn_6.configure(text="")
    elif btn_7["text"] == "":
        number = btn_6["text"]
        btn_7.configure(text=number)
        btn_6.configure(text="")
    elif btn_5["text"] == "":
        number = btn_6["text"]
        btn_5.configure(text=number)
        btn_6.configure(text="")
    elif btn_10["text"] == "":
        number = btn_6["text"]
        btn_10.configure(text=number)
        btn_6.configure(text="")

def btn5():
    if btn_1["text"] == "":
        number = btn_5["text"]
        btn_1.configure(text=number)
        btn_5.configure(text="")
    elif btn_6["text"] == "":
        number = btn_5["text"]
        btn_6.configure(text=number)
        btn_5.configure(text="")
    elif btn_9["text"] == "":
        number = btn_5["text"]
        btn_9.configure(text=number)
        btn_5.configure(text="")

def btn4():
    if btn_3["text"] == "":
        number = btn_4["text"]
        btn_3.configure(text=number)
        btn_4.configure(text="")
    elif btn_8["text"] == "":
        number = btn_4["text"]
        btn_8.configure(text=number)
        btn_4.configure(text="")

def btn3():
    if btn_4["text"] == "":
        number = btn_3["text"]
        btn_4.configure(text=number)
        btn_3.configure(text="")
    elif btn_7["text"] == "":
        number = btn_3["text"]
        btn_7.configure(text=number)
        btn_3.configure(text="")
    elif btn_2["text"] == "":
        number = btn_3["text"]
        btn_2.configure(text=number)
        btn_3.configure(text="")
def btn2():
    if btn_1["text"] == "":
        number = btn_2["text"]
        btn_1.configure(text=number)
        btn_2.configure(text="")
    elif btn_3["text"] == "":
        number = btn_2["text"]
        btn_3.configure(text=number)
        btn_2.configure(text="")
    elif btn_6["text"] == "":
        number = btn_2["text"]
        btn_6.configure(text=number)
        btn_2.configure(text="")

def btn1():
    if btn_2["text"] == "":
        number = btn_1["text"]
        btn_2.configure(text=number)
        btn_1.configure(text="")
    elif btn_5["text"] == "":
        number = btn_1["text"]
        btn_5.configure(text=number)
        btn_1.configure(text="")

def check():
    if btn_1["text"] == "1" and btn_2["text"] == "2" and btn_3["text"] == "3" and btn_4["text"] == "4" and btn_5["text"] == "5" and btn_6["text"] == "6" and btn_7["text"] == "7" and btn_8["text"] == "8" and btn_9["text"] == "9" and btn_10["text"] == "10" and btn_11["text"] == "11" and btn_12["text"] == "12" and btn_13["text"] == "13" and btn_14["text"] == "14" and btn_15["text"] == "15" and btn_["text"] == "" :
        messagebox.showinfo("تبریک","شما برنده شده اید")
    else:
        messagebox.showinfo("غلط","هنوز پازل درست نشده")



btn_1 = Button(root,text="1",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn1())
btn_1.place(x=2,y=2)

btn_2 = Button(root,text="2",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn2())
btn_2.place(x=116,y=2)

btn_3 = Button(root,text="3",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn3())
btn_3.place(x=230,y=2)

btn_4 = Button(root,text="4",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn4())
btn_4.place(x=344,y=2)

btn_5 = Button(root,text="5",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn5())
btn_5.place(x=2,y=131)


btn_6 = Button(root,text="6",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn6())
btn_6.place(x=116,y=131)

btn_7 = Button(root,text="7",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn7())
btn_7.place(x=230,y=131)

btn_8 = Button(root,text="8",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn8())
btn_8.place(x=344,y=131)

btn_9 = Button(root,text="9",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn9())
btn_9.place(x=2,y=260)

btn_10 = Button(root,text="10",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn10())
btn_10.place(x=116,y=260)

btn_11 = Button(root,text="11",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn11())
btn_11.place(x=230,y=260)

btn_12 = Button(root,text="12",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn12())
btn_12.place(x=344,y=260)

btn_13 = Button(root,text="13",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn13())
btn_13.place(x=2,y=390)

btn_14 = Button(root,text="14",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command= lambda : btn14())
btn_14.place(x=116,y=390)

btn_15 = Button(root,text="15",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn15())
btn_15.place(x=230,y=390)

btn_ = Button(root,text="",bd=1,bg="gray",fg="white",width=15,height=8,activebackground="#1B6AA5",command=lambda :btn__())
btn_.place(x=344,y=390)


btn_check = Button(root,text="check",bd=1,bg="gray",fg="white",width=20,height=3,activebackground="#1B6AA5",command=lambda :check())
btn_check.place(x=155,y=525)

btn_restart = Button(root,text="restart",bd=1,bg="gray",fg="white",width=15,height=3,activebackground="#1B6AA5",command=lambda :replace())
btn_restart.place(x=320,y=525)

btn_exit = Button(root,text="exit",bd=1,bg="gray",fg="white",width=15,height=3,activebackground="#1B6AA5",command=lambda :exit())
btn_exit.place(x=20,y=525)

replace()
root.mainloop()