from PIL import Image
import pytesseract
import easygui
from tkinter import messagebox
#=========================================
pytesseract.pytesseract.tesseract_cmd = r"tesseract address " # tesseract.exe
#=========================================
def file_open():
    path = easygui.fileopenbox()
    return path
#=========================================
text = ""
try:
    text += pytesseract.image_to_string(Image.open(file_open()),lang="fas")
except :
    messagebox.showinfo("شکست","لطفا یک عکس را انتخاب کنید")

text +=50 * "-"
print(text)