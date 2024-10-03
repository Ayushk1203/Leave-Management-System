from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


win=Tk()
win.geometry("300x500")
win.title("app")

win.configure(bg="#141414")


def bttn(x,y,text,bcolor,fcolor):
    def on_enter(e):
        button['background']=bcolor
        button['foreground']=fcolor

    def on_leave(e):
        button['background']=fcolor
        button['foreground']=bcolor

    button=Button(win,height=2,width=42,text=text,
                  fg=bcolor,
                  bg=fcolor,
                  border=0,
                  activeforeground=fcolor,
                  activebackground=bcolor,
                  command=None,)
    button.bind("<Enter>",on_enter)
    button.bind("<Leave>",on_leave)

  

    button.place(x=x,y=y)

    

 



bttn(0,0,"A C E R",'#FFCC66','#141414')
bttn(0,37,"A P P L E",'#25dae9','#141414')
bttn(0,74,"D E L L",'#f86263','#141414')
bttn(0,110,"A S U S",'#ffa157','#141414')
win.mainloop() 