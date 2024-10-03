from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class uservisiblepage:
    def __init__(self,root):
        self.root=root
        self.root.title("Leave Mangement Portal")
        self.root.geometry("1540x800+0+0")

        self.bg2=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\pexels-cristian-benavides-2665150.jpg")
        lbl_bg2=Label(self.root, image=self.bg2)
        lbl_bg2.place(x=0, y=0, relwidth=1, relheight=1)
        #=====================frame=============================================

        frame_lside=Frame(self.root, bg="lightgrey")
        frame_lside.place(x=0, y=0, relheight=1, width=300)

        frame_top=Frame(self.root, bg="lightgrey")
        frame_top.place(x=0, y=0, height=150, width=1550)

        #frame1=Frame(self.root, bg="black")
        #frame1.place(x=125, y=200, height=600, width=1300)

        self.bg1=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\haln.jpg")
        bg1_lbl=Label(self.root,image=self.bg1, bg="white",bd=10)
        bg1_lbl.place(x=50,y=20,height=139,width=200)

        frame_rside=Frame(self.root, bg="lightgrey")
        frame_rside.place( x=1500,y=0, relheight=1, width=40)

        frame_bottom=Frame(self.root, bg="lightgrey")
        frame_bottom.place( x=0,y=740, relwidth=1, height=60)

        
        #==================headings and side text labels=============================================================

        lbl_hal=Label(frame_top, text=" Hindustan Aeronautics Limited", bg="lightgrey", fg="black", font=("Old English Text MT",30,"bold"))
        lbl_hal.place(x=500, y=20)

        lbl_hal1=Label(frame_top, text=" HAL", bg="lightgrey", fg="black", font=("Old English Text MT",30,"italic"))
        lbl_hal1.place(x=710, y=70)

      

        #========================buttons left frame===================================================
        

        btn_approve=Button(frame_lside, text="Profile", fg="white", bg="green", font=("arial",15,"bold"))
        btn_approve.place(x=90, y=300)

        btn_applyleave=Button(frame_lside, text="Leave Requests", fg="white", bg="blue", font=("arial",15,"bold"))
        btn_applyleave.place(x=70, y=400)

       

        btn_pending=Button(frame_lside, text="Pending", fg="white", bg="gold", font=("arial",15,"bold"))
        btn_pending.place(x=100, y=460)

        btn_approve=Button(frame_lside, text="Approved", fg="white", bg="green", font=("arial",15,"bold"))
        btn_approve.place(x=90, y=520)

        btn_logout=Button(frame_lside, text="Logout", fg="white", bg="red", font=("arial",13,"bold"))
        btn_logout.place(x=110, y=650)

        btn_logout=Button(frame_lside, text="Exit", fg="white", bg="red", font=("arial",13,"bold"))
        btn_logout.place(x=120, y=700)

        #=============================FOOTER===================================================================
        lbl_bottom=Label(frame_bottom, text="All Rights Reserved @ Ayush Khare", bg="lightgrey", fg="black", font=("harlow solid italic",10,"bold"))
        lbl_bottom.place(x=1200, y=25)

        #==============================logo user====================================================================
        self.logo2=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\logoa.png")
        bg1_logo2=Label(frame_top,image=self.logo2, bg="white",bd=10)
        bg1_logo2.place(x=1390,y=20,height=90,width=90)

        lbl_userl=Label(frame_top, text="Admin", bg="lightgrey", fg="black", font=("arial",15,"italic"))
        lbl_userl.place(x=1400, y=120)






        






if __name__=="__main__":
    root=Tk()
    app=uservisiblepage(root)
    root.mainloop()