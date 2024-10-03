from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class useradminselectionlogin:
    def __init__(self,root):
        self.root=root
        self.root.title("Leave Mangement Portal")
        self.root.geometry("1540x800+0+0")

        self.bg2=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\pexels-cristian-benavides-2665150.jpg")
        lbl_bg2=Label(self.root, image=self.bg2)
        lbl_bg2.place(x=0, y=0, relwidth=1, relheight=1)
        #=====================frame and logo=============================================
        
        self.bg1=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\Hindustan_Aeronautics_Limited_Logo.svg__43966__thumb.png")
        bg1_lbl=Label(self.root,image=self.bg1, bg="black")
        bg1_lbl.place(x=1000,y=120,width=400,height=200)
        
        frame=Frame(self.root, bg="black")
        frame.place(x=1000, y=300, height=400, width=400)

        lbl_Frame=Label(frame, text="LOGIN AS", bg="grey",fg="white", font=("Algerian",30,"bold"))
        lbl_Frame.pack(side=TOP,fill=X)

        btn_User=Button(frame, text="Admin", bg="red", fg="white",font=("Bradley Hand ITC",25,"bold"))
        btn_User.place(x=135, y=120)

        btn_Admin=Button(frame, text="Employee", bg="red", fg="white",font=("Bradley Hand ITC",25,"bold"))
        btn_Admin.place(x=120, y=220)

        






if __name__=="__main__":
    root=Tk()
    app=useradminselectionlogin(root)
    root.mainloop()