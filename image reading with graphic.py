from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter
import pytesseract as ts
from PIL import Image
import pyttsx3
import cv2
#defining my window
root=Tk()
root.config(bg="Gray")
root.maxsize(1300,700)
root.geometry('1300x700+100+60')
root.minsize(1300,700)
root.title("Extracting Text From Image")
#variable defining
img_name=StringVar()
img_type=StringVar()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#-----------function-------------
def resize_img():
    #image resizing
    img=cv2.imread("%s.%s"%(img_name.get(),img_type.get()))
    scale_percent=0.20
    width=int(img.shape[1]*scale_percent)
    height=int(img.shape[0]*scale_percent)
    dimension=(width,height)
    resized=cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)
    cv2.imwrite("resized_1.png",resized)
    im=PhotoImage(file="resized_1.png")
    img_labe.config(image=im)
    img_labe.image=im
def exite():
    root.destroy()
def extract_text():
    if img_name.get()!='' and img_type.get()!='':
        global new
        img=Image.open('%s.%s'%(img_name.get(),img_type.get()))
        new=ts.image_to_string(img)
        text.insert(END,new)
        resize_img()
    else:
        tkinter.messagebox.showinfo('Program','Please enter image name and type')

def speak_t(new):
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    speak(new)
def res():
    img_name.set("")
    image_type_cbo.current(0)
    text.delete("1.0",END)
    im=PhotoImage(file="kl.png")
    img_labe.config(image=im)
    img_labe.image=im
#-------------defining frame---------
top_frame=Frame(root,relief=RIDGE,bd=5)
top_frame.pack(side=TOP)#top frame
bottom_frame=Frame(root,relief=RIDGE,bd=5)
bottom_frame.pack(side=BOTTOM)#buttom frame


#top leabel---------------------------
title_lable=Label(top_frame,text="Text Extracting",font=('arial 16 bold'),bd=5).pack()
#buttom frame------------
bottom_frame_left=Frame(bottom_frame,relief=RIDGE,bd=5)
bottom_frame_left.pack(side=LEFT,anchor='n')#left frfame

#image frame
img_frame=Frame(bottom_frame_left,relief=RIDGE,bd=5)
img_frame.pack(side=BOTTOM,anchor='nw')
im=PhotoImage(file="kl.png")
img_labe=Label(img_frame,image=im,bg="green")
img_labe.pack(side=BOTTOM,anchor='ne')
#label_frame---
label_frame=Frame(bottom_frame_left,relief=RIDGE,bd=5)
label_frame.pack(side=LEFT,anchor='ne')

#Labels

name_label=Label(label_frame,text="Image Path",font=('arial 16 bold'),width=18,bd=5)
name_label.pack(side=TOP)
image_type=Label(label_frame,text="Image Type",font=('arial 16 bold'),width=18,bd=5)
image_type.pack(side=TOP)
#entryframe----
bottom_frame_right=Frame(bottom_frame_left,relief=RIDGE,bd=5)
bottom_frame_right.pack(side=LEFT)#right frame
#entry image name
entry_box=Entry(bottom_frame_right,textvar=img_name,font=('arial 16 bold'),width=18,bd=5)
entry_box.pack(side=TOP)
#entering image type-----

image_type_cbo=tkinter.ttk.Combobox(bottom_frame_right, textvar=img_type, state='readonly', font=('arial',16,'bold'), width =15)
image_type_cbo.pack(side=TOP)
image_type_cbo['value']=("--Select--","png","jpg","jpeg")
image_type_cbo.current(0)
#text frame---------------
text_frame=Frame(bottom_frame,relief=RIDGE,bd=5)
text_frame.pack(side=RIGHT)
#------------button------------
butn_frame=Frame(bottom_frame_right,relief=RIDGE,bd=5)
butn_frame.pack(side=BOTTOM)
#--------extract-----------
e_butt=Button(label_frame,text="Extract",font=('arial 10 bold'),bg='yellow',width=28,bd=5,command=extract_text)
e_butt.pack(side=TOP)
#-------read----------------
r_butt=Button(butn_frame,text="Read",font=('arial 10 bold'),bg='pink',width=28,bd=5,command=lambda:speak_t(new))
r_butt.pack(side=TOP)
#----reset button-----------------
rs_btn=Button(label_frame,text="Reset",font=('arial 10 bold'),bg='orange',width=28,bd=5,command=res)
rs_btn.pack(side=TOP)
#-------exit----------------
ex_btn=Button(butn_frame,text="Exit",font=('arial 10 bold'),bg='red',width=28,bd=5,command=exite)
ex_btn.pack(side=TOP)
#---------text----------------

text=Text(text_frame,height=40,width=100)
text.pack(side=BOTTOM)
root.mainloop()
