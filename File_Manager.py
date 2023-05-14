from tkinter import Tk,filedialog,messagebox,Label,Button
import pyautogui
import shutil
import os
import easygui

root = Tk()
root.geometry("300x400")
root.resizable(False,False)
root.configure(bg="gray")
root.title("File manager")
# ==================================================
def file_open():
    path = easygui.fileopenbox()
    return path


def folder_select():
    path = filedialog.askdirectory()
    return path

# ==================================================
def start_file():
    path = file_open()
    os.startfile(path)
# ==================================================

def deletfile():
    try:
        path = file_open()
        os.remove(path)
        messagebox.showinfo("انجام شد","فایل با موفقیت حذف شد")
    except:
        messagebox.showinfo("انجام نشد", "عملیات حذف با شکست مواجه شد")
# ==================================================
def rename():
    try:
        path = file_open()
        path_1 = os.path.dirname(path)
        exten = os.path.splitext(path)[1]
        name = input("esm jadid ra vared konid : ")
        path_2 = os.path.join(path_1,name + exten)
        os.rename(path,path_2)
        messagebox.showinfo("انجام شد","اسم فایل با موفقیت تغییر پیدا کرد")
    except:
        messagebox.showinfo("شکست خورد","اسم فایل هیچ تغییری پیدا نکرد")
# ===================================================
def copy_file():
    path = file_open()
    direc = folder_select()
    try:
        shutil.copy(path,direc)
        messagebox.showinfo("کپی شد","فایل با موفقیت کپی شد ")
    except:
        messagebox.showinfo("شکست","عملیات کپی شکست خورد")
# ==================================================
def movefile():
    path = file_open()
    folder = folder_select()
    if path==folder:
        messagebox.showinfo("شکست","محل انتقال مشکل دارد")
    else:
        try:
            shutil.move(path,folder)
            messagebox.showinfo("موفق","فایل انتقال یافت")
        except:
            messagebox.showinfo("مشکل","عملیات انتقال موفقیت آمیز نبود")
# ==================================================
def newfolder():
    path = folder_select()
    name = input("name new folder :  ")
    path = os.path.join(path,name)
    try:
        os.mkdir(path)
        messagebox.showinfo("موفق","فولدر جدید ایجاد شد")
    except:
        messagebox.showinfo("موفق نبود","فولدر جدید ایجاد نشد")
# ====================================================
def removefolder():
    path= folder_select()
    try:
        os.rmdir(path)
        messagebox.showinfo("موفق", "فولدر حذف شد")
    except:
        messagebox.showinfo("شکست","عملیات با شکست مواجه شد")

# =====================================================
def listfile():
    path = folder_select()
    try:
        file_list = sorted(os.listdir(path))
        for i in file_list:
            print(i)
    except:
        messagebox.showinfo("شکست","فولدر مورد نظر لیست نشد")
# ======================================================
def exit():
    pyautogui.hotkey('alt','f4')


# ==================================================

entry_open = Button(root,text="open file",width="15",command=lambda :start_file())
entry_open.place(x=90,y=10)

entry_delete = Button(root,text="delet file",width="15",command=lambda :deletfile())
entry_delete.place(x=90,y=50)

entry_rename = Button(root,text="rename file ",width="15",command=lambda :rename())
entry_rename.place(x=90,y=90)

entry_copy = Button(root,text="copy file",width="15",command=lambda :copy_file())
entry_copy.place(x=90,y=130)

entry_move = Button(root,text="move file",width="15",command=lambda :movefile())
entry_move.place(x=90,y=170)

entry_newfolder = Button(root,text="newfolder",width="15",command=lambda :newfolder())
entry_newfolder.place(x=90,y=210)

entry_removefolder = Button(root,text="remove folder",width="15",command=lambda :removefolder())
entry_removefolder.place(x=90,y=250)

entry_list = Button(root,text="list file",width="15",command=lambda :listfile())
entry_list.place(x=90,y=290)

entry_list = Button(root,text="exit",width="15",command=lambda :exit())
entry_list.place(x=90,y=330)



root.mainloop()
