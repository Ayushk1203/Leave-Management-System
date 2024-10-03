from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class adminlogin:
    def __init__(self,root):
        self.root=root
        self.root.title("Leave Mangement Portal")
        self.root.geometry("1540x800+0+0")

        self.bg2=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\pexels-cristian-benavides-2665150.jpg")
        lbl_bg2=Label(self.root, image=self.bg2)
        lbl_bg2.place(x=0, y=0, relwidth=1, relheight=1)
        #=====================frame=============================================
        frame1=Frame(self.root, bg="black")
        frame1.place(x=900, y=300, height=400, width=500)

        self.bg1=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\Hindustan_Aeronautics_Limited_Logo.svg__43966__thumb.png")
        bg1_lbl=Label(self.root,image=self.bg1, bg="black")
        bg1_lbl.place(x=900,y=100,width=500,height=200)

        lbl_Frame=Label(frame1, text="ADMIN LOGIN", bg="grey",fg="white", font=("Algerian",30,"bold"))
        lbl_Frame.pack(side=TOP,fill=X)

        lbl_email=Label(frame1, text=" Email :", bg="black", fg="white", font=("Ink Free",20,"bold"))
        lbl_email.place(x=25, y=120)

        ent_email=Entry(frame1, bg="lightgrey",font=("Cosmic Sans MS",15))
        ent_email.place(x=210, y=125)

        lbl_password=Label(frame1, text=" Password :", bg="black", fg="white", font=("Ink Free",20,"bold"))
        lbl_password.place(x=25, y=200)

        ent_password=Entry(frame1, bg="lightgrey",font=("Cosmic Sans MS",15))
        ent_password.place(x=210, y=205)

        btn_login=Button(frame1, text="Login",bg="red",fg="white" ,font=("algerian",20,"bold") )
        btn_login.place(x=200,y=320)

        






if __name__=="__main__":
    root=Tk()
    app=adminlogin(root)
    root.mainloop()