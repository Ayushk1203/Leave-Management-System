from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Welcomepage:
    def __init__(self,root):
        self.root=root
        self.root.title("Leave Management System")
        self.root.geometry("1540x800+0+0")

        #======================================bgimage===================================================================================
        self.bg=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\pexels-khalid-aljmman-7155378.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        #======================================frame and logo==================================================================
        
        frame=Frame(self.root,bg="black")
        frame.place(x=550,y=250,height=400,width=400) 

        self.bg1=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\Hindustan_Aeronautics_Limited_Logo.svg__43966__thumb.png")
        bg1_lbl=Label(self.root,image=self.bg1, bg="black")
        bg1_lbl.place(x=550,y=150,width=400,height=200)


        #==============================Welcome page texts==================================================
        welcome_lbl=Label(frame,text="WELCOME  TO",font=("forte",30,"bold") ,fg="white", bg="black")
        welcome_lbl.place(x=70,y=100)

        welcome_lbl=Label(frame,text="Leave Management Portal",font=("forte",20,"bold") ,fg="white", bg="black")
        welcome_lbl.place(x=35,y=150)

        btn_login=Button(frame, text="CONTINUE",bg="grey",fg="Black" ,font=("algerian",20,"bold") )
        btn_login.place(x=125,y=220)

        welcome_lbl=Label(frame,text="Developed By : Ayush Khare",font=("Ink Free",20,"bold") ,fg="white", bg="black")
        welcome_lbl.place(x=35,y=320)

        #===============================
        #frame=Frame(self.root,bg="black")
        #frame.place(x=1000,y=20,height=100,width=400)  
        # ==============================================FUNCTIONS===================================================
                                






if __name__=="__main__":
    root=Tk()
    app=Welcomepage(root)
    root.mainloop()
