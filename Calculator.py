import tkinter.messagebox
from tkinter import *
import pyautogui
import easygui
# =========================================
root = Tk()
root.title("calculator")
root.geometry("300x500")
root.configure(bg="gray")
root.resizable(width=False,height=False)
# +++++++++++++++++++++++++++++++++++++++++
num_1=StringVar()
num_2=StringVar()
res=StringVar()
# =========================================


entry_1 = Entry(root,textvariable=num_1)
entry_1.place(x=110,y=20)
label_1=Label(root,text="adad aval",bg="gray")
label_1.place(x=30,y=20)
# -------------------------------------------
entry_2 = Entry(root,textvariable=num_2)
entry_2.place(x=110,y=60)
label_2=Label(root,text="adad dovom",bg="gray")
label_2.place(x=12,y=60)
# --------------------++---------------------
btn_1=Button(root,text="+",width=15,command=lambda :plus())
btn_1.place(x=10,y=90)
# +++++++++++++++------++++++++++++++++++++++
btn_2=Button(root,text="-",width=15,command=lambda :minus())
btn_2.place(x=160,y=90)
# ---------------////------------------------
btn_3=Button(root,text="/",width=15,command=lambda :div())
btn_3.place(x=160,y=140)
# --------------******-----------------------
btn_4=Button(root,text="*",width=15,command=lambda :mul())
btn_4.place(x=10,y=140)
# -------------------------------------------

# -------------------------------------------
entry_3 = Entry(root,textvariable=res)
entry_3.place(x=75,y=190)
label_3=Label(root,text="result",bg="gray")
label_3.place(x=30,y=190)
# -------------------------------------------
btn_6_1=Button(root,text="1",width=10,command=lambda :adad_1())
btn_6_1.place(x=10,y=250)
# -------------------------------------------
btn_6_2=Button(root,text="2",width=10,command=lambda :adad_2())
btn_6_2.place(x=100,y=250)
# -------------------------------------------
btn_7_3=Button(root,text="3",width=10,command=lambda :adad_3())
btn_7_3.place(x=190,y=250)
# -------------------------------------------
btn_8_4=Button(root,text="4",width=10,command=lambda :adad_4())
btn_8_4.place(x=10,y=290)
# -------------------------------------------
btn_9_5=Button(root,text="5",width=10,command=lambda :adad_5())
btn_9_5.place(x=100,y=290)
# -------------------------------------------
btn_10_6=Button(root,text="6",width=10,command=lambda :adad_6())
btn_10_6.place(x=190,y=290)
# -------------------------------------------
btn_11_7=Button(root,text="7",width=10,command=lambda :adad_7())
btn_11_7.place(x=10,y=330)
# -------------------------------------------
btn_12_8=Button(root,text="8",width=10,command=lambda :adad_8())
btn_12_8.place(x=100,y=330)
# -------------------------------------------
btn_13_9=Button(root,text="9",width=10,command=lambda :adad_9())
btn_13_9.place(x=190,y=330)
# -------------------------------------------
btn_14_0=Button(root,text="0",width=10,command=lambda :adad_0())
btn_14_0.place(x=100,y=370)
# -------------------------------------------
btn_15_exit=Button(root,text="exit",width=10,command=lambda :exit_1())
btn_15_exit.place(x=10,y=370)
# -------------------------------------------
btn_16_ace=Button(root,text="ACE",width=10,command=lambda :ace())
btn_16_ace.place(x=190,y=370)
# ===============================buttom===========================================================
def exit_1():
    pyautogui.hotkey('alt','f4')
def adad_1():
    pyautogui.press("1")
def adad_2():
    pyautogui.press("2")
def adad_3():
    pyautogui.press("3")
def adad_4():
    pyautogui.press("4")
def adad_5():
    pyautogui.press("5")
def adad_6():
    pyautogui.press("6")
def adad_7():
    pyautogui.press("7")
def adad_8():
    pyautogui.press("8")
def adad_9():
    pyautogui.press("9")
def adad_0():
    pyautogui.press("0")
def ace():
    num_1.set("")
    num_2.set("")
    res.set("")

# ===============================buttom===========================================================
def plus():
    try:
        value=float(entry_1.get()) + float(entry_2.get())
        res.set(value)
    except:
        errorm("error")
def minus():
    try:
        value=float(entry_1.get()) - float(entry_2.get())
        res.set(value)
    except:
        errorm("error")
def mul():
    try:
        value=float(entry_1.get()) * float(entry_2.get())
        res.set(value)
    except:
        errorm("error")
def div():
    if num_2.get() == "0":
        errorm("division zero error")
    elif num_2.get() != "0":
        try:
            value=float(entry_1.get()) / float(entry_2.get())
            res.set(value)
        except:
            errorm("error")

# =========================================
def errorm(ms):
    if ms== "error":
        tkinter.messagebox.showerror('ERROR',"something went wrong")
    elif ms =="division zero error":
        tkinter.messagebox.showerror('ERROR',"Can Not Divide By 0")


# ======================================================


root.mainloop()