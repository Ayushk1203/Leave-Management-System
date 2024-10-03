from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from tkcalendar import *



win=tk.Tk()




#==========================================================================================================================
#=================================            PAGE 1                =======================================================

#============================================PAGE FRAME=====================================================================
page1=Frame(win)
page1.place(x=0,y=0,relheight=1,relwidth=1)   
#=======================================BACKGROUND IMAGE====================================================================
bg_page1=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\backgroundimage.jpg")
bg_lbl_page1=Label(page1,image=bg_page1)
bg_lbl_page1.place(x=0,y=0,relwidth=1,relheight=1)
        #======================================frame and logo==================================================================
        
frame_page1=Frame(bg_lbl_page1,bg="black")
frame_page1.place(x=550,y=250,height=400,width=400) 

bg1_page1=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\hallogo.jfif")
bg1_lbl_page1=Label(bg_lbl_page1,image=bg1_page1, bg="black")
bg1_lbl_page1.place(x=550,y=150,width=400,height=200)


        #==============================Welcome page texts==================================================
welcome_lbl=Label(frame_page1,text="WELCOME  TO",font=("forte",30,"bold") ,fg="white", bg="black")
welcome_lbl.place(x=70,y=100)

welcome_lbl=Label(frame_page1,text="Leave Management Portal",font=("forte",20,"bold") ,fg="white", bg="black")
welcome_lbl.place(x=35,y=150)

#=================================FUNCTION FOR BUTTON===========================================================
def bttn(button,frame,x,y,h,w,text,bcolor,fcolor,fn,size,sty,cmd,tv):
    def on_enter(e):
        button['background']=bcolor
        button['foreground']=fcolor

    def on_leave(e):
        button['background']=fcolor
        button['foreground']=bcolor

    button=Button(frame,height=h,width=w,text=text,
                  fg=bcolor,
                  bg=fcolor,
                  font=(fn,size,sty),
                  border=0,
                  activeforeground=fcolor,
                  activebackground=bcolor,
                  textvariable=tv,
                  command=cmd,)
    button.bind("<Enter>",on_enter)
    button.bind("<Leave>",on_leave)

  

    button.place(x=x,y=y)

#===============================================================================================================

bttn("btn_page1",frame_page1,0,220,2,25,"C O N T I N U E",'#FFCC66','black',"forte",20,"bold",lambda:page2.tkraise(),None)

welcome_lbl=Label(frame_page1,text="Developed By : Ayush Khare",font=("Ink Free",20,"bold") ,fg="white", bg="black")
welcome_lbl.place(x=35,y=320)

#==========================================================================================================================
#=============================================PAGE 2=======================================================================
#==========================================================================================================================
#===========================================================================================================================
page2=Frame(win)
page2.place(x=0,y=0,relheight=1,relwidth=1)

bg2_page2=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\backgroundimage.jpg")
lbl_bg2_page2=Label(page2, image=bg2_page2)
lbl_bg2_page2.place(x=0, y=0, relwidth=1, relheight=1)
        #=====================frame and logo=============================================
        
bg1_page2=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\hallogo.jfif")
bg1_lbl_page2=Label(lbl_bg2_page2,image=bg1_page2, bg="black")
bg1_lbl_page2.place(x=1000,y=120,width=400,height=200)
        
frame_page2=Frame(lbl_bg2_page2, bg="black")
frame_page2.place(x=1000, y=300, height=400, width=400)


bttn("back_pag2_page1",frame_page2,0,0,1,10,"⇦ Back",'orange','black',"bradley hand ITC",15,"bold",lambda:page1.tkraise(),None)


#bttn("btn_page1",0,220,2,25,"C O N T I N U E",'#FFCC66','black',"forte",20,"bold",lambda:page2.tkraise(),None)
bttn("lbl_Frame_page2",frame_page2,1,50,1,15,"L O G I N   A S",'white','black',"Algerian",30,"bold",None,None)

#lbl_Frame_page2=Label(frame_page2, text="LOGIN AS", bg="grey",fg="white", font=("Algerian",30,"bold"))
#lbl_Frame_page2.pack(side=TOP,fill=X)

bttn("btn_Admin_page2",frame_page2,0,170,2,20,"Admin",'lightblue','black',"Bradley Hand ITC",25,"bold",lambda:page4.tkraise(),None)

#btn_Admin_page2=Button(frame_page2, text="Admin",command=lambda:page4.tkraise(), bg="red", fg="white",font=("Bradley Hand ITC",25,"bold"))
#btn_Admin_page2.place(x=135, y=120)

bttn("btn_Employee_page2",frame_page2,0,290,2,20,"Employee",'lightblue','black',"Bradley Hand ITC",25,"bold",lambda:page3.tkraise(),None)

#btn_Employee_page2=Button(frame_page2, text="Employee",command=lambda:page3.tkraise(), bg="red", fg="white",font=("Bradley Hand ITC",25,"bold"))
#btn_Employee_page2.place(x=120, y=220)

#==========================================================================================================================
#=============================================PAGE 3=======================================================================
#==========================================================================================================================
#==========================================================================================================================

page3=Frame(win)
page3.place(x=0,y=0,relheight=1,relwidth=1)

#=======================functions page3=======================================================
#==================================================================================================================



def login():
    if ent_eid_page3.get()=="" and ent_password_page3.get()=="":
        messagebox.showerror("Error","Please fill your EmployeeID and Password")
    elif ent_eid_page3.get()=="":
        messagebox.showerror("Error","Please fill your employeeid")
    elif ent_password_page3.get()=="":
        messagebox.showerror("Error","Please fill your password")
    else:
        try:
             conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
             my_cursor=conn.cursor()
        except:
            messagebox.showerror("Error","Connectivity Issue")
            return
        query='select * from employee where EID=%s and Password=%s'
        my_cursor.execute(query,(ent_eid_page3.get(),ent_password_page3.get()))
        row=my_cursor.fetchone()
        if row==None:
             messagebox.showerror("Error","User not found")
        else:
             page5.tkraise()
            
        conn.commit()
        conn.close()





bg2_page3=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\backgroundimage.jpg")
lbl_bg2_page3=Label(page3, image=bg2_page3)
lbl_bg2_page3.place(x=0, y=0, relwidth=1, relheight=1)
#=====================frame=============================================
frame1_page3=Frame(page3, bg="black")
frame1_page3.place(x=950, y=300, height=400, width=500)
bg1_page3=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\hallogo.jfif")
bg1_lbl_page3=Label(page3,image=bg1_page3, bg="black")
bg1_lbl_page3.place(x=950,y=100,width=500,height=200)

bttn("back_pag2_page1",frame1_page3,0,0,1,10,"⇦ Back",'orange','black',"bradley hand ITC",15,"bold",lambda:page2.tkraise(),None)

bttn("lbl_Frame_page3",frame1_page3,0,51,1,19,"EMPLOYEE   LOGIN",'white','black',"Algerian",30,"bold",None,None)

#lbl_Frame_page3=Label(frame1_page3, text="USER LOGIN", bg="grey",fg="white", font=("Algerian",30,"bold"))
#lbl_Frame_page3.pack(side=TOP,fill=X)

lbl_eid_page3=Label(frame1_page3, text=" Employee ID :", bg="black", fg="white", font=("Ink Free",20,"bold"))
lbl_eid_page3.place(x=25, y=150)

ent_eid_page3=Entry(frame1_page3,cursor="hand1",bg="lightgrey",font=("Cosmic Sans MS",15))
ent_eid_page3.place(x=225, y=155)







lbl_password_page3=Label(frame1_page3, text=" Password :", bg="black", fg="white", font=("Ink Free",20,"bold"))
lbl_password_page3.place(x=25, y=230)

ent_password_page3=Entry(frame1_page3, bg="lightgrey",font=("Cosmic Sans MS",15))
ent_password_page3.place(x=225, y=235)

bttn("btn_login_page3",frame1_page3,0,300,2,24,"Login",'lightblue','black',"algerian",25,"bold",login,None)

#btn_login_page3=Button(frame1_page3, text="Login",command=login,bg="red",fg="white" ,font=("algerian",20,"bold") )
#btn_login_page3.place(x=200,y=320)


#============================================================================================================================
#===================================PAGE 4===================================================================================
#============================================================================================================================
#============================================================================================================================
#===================================Page 4====================================================================
#============================================================================================================
var_aid=StringVar()
var_password_admin=StringVar()



#============================================================================================================ 
#=========================================Frame for page 4====================================================
page4=Frame(win)
page4.place(x=0,y=0,relheight=1,relwidth=1)

#==================================Background image of page 4=================================================
bg2_page4=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\backgroundimage.jpg")
lbl_bg2_page4=Label(page4, image=bg2_page4)
lbl_bg2_page4.place(x=0, y=0, relwidth=1, relheight=1)
#=====================Middle Black Frame =============================================
frame1_page4=Frame(page4, bg="black")
frame1_page4.place(x=950, y=300, height=400, width=500)

#============================Back Button===============================================
bttn("back_pag2_page1",frame1_page4,0,0,1,10,"⇦ Back",'orange','black',"bradley hand ITC",15,"bold",lambda:page2.tkraise(),None)
#============================Logo Image=======================================================
bg1_page4=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\hallogo.jfif")
bg1_lbl_page4=Label(page4,image=bg1_page4, bg="black")
bg1_lbl_page4.place(x=950,y=100,width=500,height=200)
#=================================Admin login Label Button ====================================================
bttn("lbl_Frame_page4",frame1_page4,0,51,1,19,"ADMIN  LOGIN",'white','black',"Algerian",30,"bold",None,None)

#lbl_Frame_page4=Label(frame1_page4, text="ADMIN LOGIN", bg="grey",fg="white", font=("Algerian",30,"bold"))
#lbl_Frame_page4.pack(side=TOP,fill=X)
#=======================Label and Entry for Admin login and Password==============================================================
lbl_aid_page6=Label(frame1_page4, text=" Admin ID :", bg="black", fg="white", font=("Ink Free",20,"bold"))
lbl_aid_page6.place(x=25, y=150)

ent_aid_page6=Entry(frame1_page4,textvariable=var_aid, bg="lightgrey",font=("Cosmic Sans MS",15))
ent_aid_page6.place(x=210, y=155)

lbl_password=Label(frame1_page4, text=" Password :", bg="black", fg="white", font=("Ink Free",20,"bold"))
lbl_password.place(x=25, y=230)

ent_password=Entry(frame1_page4,textvariable=var_password_admin, bg="lightgrey",font=("Cosmic Sans MS",15))
ent_password.place(x=210, y=235)

#==================================Login Button and function=========================================================
def login_admin():
    if ent_aid_page6.get()=="" and ent_password.get()=="":
        messagebox.showerror("Error","Please fill your EmployeeID and Password")
    elif ent_aid_page6.get()=="":
        messagebox.showerror("Error","Please fill your employeeid")
    elif ent_password.get()=="":
        messagebox.showerror("Error","Please fill your password")
    else:
        try:
             conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
             my_cursor=conn.cursor()
        except:
            messagebox.showerror("Error","Connectivity Issue")
            return
        query='select * from admin where AID=%s and PASSWORD=%s'
        my_cursor.execute(query,(ent_aid_page6.get(),ent_password.get()))
        row=my_cursor.fetchone()
        if row==None:
             messagebox.showerror("Error","User not found")
        else:
             page6.tkraise()
            
        conn.commit()
        conn.close()

bttn("btn_login_page4",frame1_page4,0,300,2,24,"Login",'lightblue','black',"algerian",25,"bold",login_admin,None)

#btn_login=Button(frame1_page4,command=login_admin, text="Login",bg="red",fg="white" ,font=("algerian",20,"bold") )
#btn_login.place(x=200,y=320)
#============================================================================================================================
#============================================================================================================================
#============================================PAGE5===========================================================================
#============================================================================================================================
#============================================================================================================================


#++++++++++++++++++++++++++++++++++++++++++Functions+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def logout():
    page2.tkraise()

def exit():
    page5.destroy()
    win.destroy()



#+++++++++++++++++++++++++++++++++++++++++++=++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#===========================================================================================================================
#=================================================Variables declaration=====================================================

var_eid=StringVar()
var_name=StringVar()
var_department=StringVar()
var_noofdays=StringVar()
var_fromdate=StringVar()
var_todate=StringVar()
var_reason=StringVar()
var_status=StringVar()

page5=Frame(win)
page5.place(x=0,y=0,relheight=1,relwidth=1)

#===========================================Functions========================================================================


#==========================================pending button function========================================================
def table_pending():
    frame=Frame(page5,bg="white")
    frame.place(x=380,y=200,width=900,height=500)

    def btn_Close():
        frame.destroy()
        frame_table.destroy()

    bttn("button_back",frame,0,400,3,56,"Close Tab",'red','black',"forte",20,"bold",btn_Close,None)

    frame_table=Frame(page5,bg="white")
    frame_table.place(x=380,y=200,width=900,height=400)

    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                     background="silver",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="grey"
                                )
    style.map('Treeview',background=[('selected','yellow')])

    scroll_x=ttk.Scrollbar(frame_table,orient="horizontal")
    scroll_y=ttk.Scrollbar(frame_table,orient="vertical")

    leave_table=ttk.Treeview(frame_table,column=("EID","name","department","noofdays","fromdate","todate","reason","status"),
    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x=ttk.Scrollbar(command=leave_table.xview)
    scroll_x=ttk.Scrollbar(command=leave_table.yview)


    leave_table.heading("EID",text="Employee ID")
    leave_table.heading("name",text="Name")
    leave_table.heading("department",text="Department")
    leave_table.heading("noofdays",text="Number Of Days")
    leave_table.heading("fromdate",text="From Date")
    leave_table.heading("todate",text="To Date")
    leave_table.heading("reason",text="Reason")
    leave_table.heading("status",text="Status")

    leave_table["show"]="headings"

    leave_table.column("EID",width=100)
    leave_table.column("name",width=100)
    leave_table.column("department",width=100)
    leave_table.column("noofdays",width=100)
    leave_table.column("fromdate",width=100)
    leave_table.column("todate",width=100)
    leave_table.column("reason",width=100)
    leave_table.column("status",width=100)
    leave_table.pack(fill=BOTH,expand=1)

    

    conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
    my_cursor=conn.cursor()
    
    query="SELECT EMPLOYEEID,NAME,DEPARTMENT,NO_OF_DAYS,FROM_DATE,TO_DATE,REASON,STATUS FROM EMPLOYEE,LEAVE_ENTRY WHERE EID=EMPLOYEEID AND STATUS='pending'"
    my_cursor.execute(query)
    try:
        rows=my_cursor.fetchall()
        for i in rows:
            leave_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("error","error")






#===========================================================================================================================
#==============================================approved button function=====================================================

def table_approved():

    frame=Frame(page5,bg="white")
    frame.place(x=380,y=200,width=900,height=500)

    
    def btn_Close():
        frame.destroy()
        frame_table.destroy()

    bttn("button_back",frame,0,400,3,56,"Close",'red','black',"forte",20,"bold",btn_Close,None)

    frame_table=Frame(page5,bg="white")
    frame_table.place(x=380,y=200,width=900,height=400)
    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                     background="silver",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="grey"
                                )
    style.map('Treeview',background=[('selected','lightblue')])
    scroll_x=ttk.Scrollbar(frame_table,orient="horizontal")
    scroll_y=ttk.Scrollbar(frame_table,orient="vertical")

    leave_table=ttk.Treeview(frame_table,column=("EID","name","department","noofdays","fromdate","todate","reason","status"),
    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x=ttk.Scrollbar(command=leave_table.xview)
    scroll_x=ttk.Scrollbar(command=leave_table.yview)

                   


    leave_table.heading("EID",text="Employee ID")
    leave_table.heading("name",text="Name")
    leave_table.heading("department",text="Department")
    leave_table.heading("noofdays",text="Number Of Days")
    leave_table.heading("fromdate",text="From Date")
    leave_table.heading("todate",text="To Date")
    leave_table.heading("reason",text="Reason")
    leave_table.heading("status",text="Status")

    leave_table["show"]="headings"

    leave_table.column("EID",width=100)
    leave_table.column("name",width=100)
    leave_table.column("department",width=100)
    leave_table.column("noofdays",width=100)
    leave_table.column("fromdate",width=100)
    leave_table.column("todate",width=100)
    leave_table.column("reason",width=100)
    leave_table.column("status",width=100)
    leave_table.pack(fill=BOTH,expand=1)
    



    def btn_Close():
        frame.destroy()
        frame_table.destroy()

    bttn("button_back",frame,0,400,3,56,"Close Tab",'red','black',"forte",20,"bold",btn_Close,None)
    
   
    
    
    conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
    my_cursor=conn.cursor()
    ent_eid_page3.get()
    try:
        query="select EMPLOYEEID,NAME,DEPARTMENT,NO_OF_DAYS,FROM_DATE,TO_DATE,REASON,STATUS from employee,leave_entry where EID=EMPLOYEEID and STATUS='APPROVED'"
        
        
        my_cursor.execute(query)
        messagebox.showinfo("success","success")
    except:
        messagebox.showinfo("error","error") 

    try:
        rows=my_cursor.fetchall()
        for i in rows:
            leave_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("error","error")

def table_rejected():
    frame=Frame(page5,bg="white")
    frame.place(x=380,y=200,width=900,height=500)

    def btn_Close():
        frame.destroy()
        frame_table.destroy()

    bttn("button_back",frame,0,400,3,56,"Close Tab",'red','black',"forte",20,"bold",btn_Close,None)

    

    frame_table=Frame(page5,bg="white")
    frame_table.place(x=380,y=200,width=900,height=400)
    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                     background="silver",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="grey"
                                )
    style.map('Treeview',background=[('selected','lightblue')])
    scroll_x=ttk.Scrollbar(frame_table,orient="horizontal")
    scroll_y=ttk.Scrollbar(frame_table,orient="vertical")

    leave_table=ttk.Treeview(frame_table,column=("EID","name","department","noofdays","fromdate","todate","reason","status"),
    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x=ttk.Scrollbar(command=leave_table.xview)
    scroll_x=ttk.Scrollbar(command=leave_table.yview)

                   


    leave_table.heading("EID",text="Employee ID")
    leave_table.heading("name",text="Name")
    leave_table.heading("department",text="Department")
    leave_table.heading("noofdays",text="Number Of Days")
    leave_table.heading("fromdate",text="From Date")
    leave_table.heading("todate",text="To Date")
    leave_table.heading("reason",text="Reason")
    leave_table.heading("status",text="Status")

    leave_table["show"]="headings"

    leave_table.column("EID",width=100)
    leave_table.column("name",width=100)
    leave_table.column("department",width=100)
    leave_table.column("noofdays",width=100)
    leave_table.column("fromdate",width=100)
    leave_table.column("todate",width=100)
    leave_table.column("reason",width=100)
    leave_table.column("status",width=100)
    leave_table.pack(fill=BOTH,expand=1)
    
    
    
    
    conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
    my_cursor=conn.cursor()
    
    query="SELECT EMPLOYEEID,NAME,DEPARTMENT,NO_OF_DAYS,FROM_DATE,TO_DATE,REASON,STATUS FROM EMPLOYEE,LEAVE_ENTRY WHERE EID=EMPLOYEEID AND STATUS='REJECTED'"
    my_cursor.execute(query)
    try:
        rows=my_cursor.fetchall()
        for i in rows:
            leave_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("error","error")
#=============================================================================================================================
def apply_leave():

    #====================================
    def tabledata_from_applyleaveform():
        empid=entry_eid.get()
        name_emp=entry_name.get()
        department_emp=entry_department.get()
        noofdays_emp=entry_noofdays.get()
        fromdate_emp=cal1.get()
        todate_emp=cal2.get()
        reason_emp=entry_reason.get()
        status_emp="pending"
        if entry_eid.get()=="" or entry_name.get()=="" or entry_department.get()=="" or cal1.get()=="" or cal2.get()=="" or var_noofdays.get()=="":
            messagebox.showerror("Error","Please fill all the necessary details")    
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
            my_cursor=conn.cursor()
            
            
            query="INSERT INTO leave_entry (EMPLOYEEID,NO_OF_DAYS,FROM_DATE,TO_DATE,REASON,STATUS) VALUES (%s,%s,%s,%s,%s,%s)"
            vals=(empid,noofdays_emp,fromdate_emp,todate_emp,reason_emp,status_emp)
            my_cursor.execute(query,vals)
            messagebox.showinfo("success","success")
            conn.commit()
            conn.close()
            
    #====================================
    frame_applyleave=Frame(page5,bg="black")
    frame_applyleave.place(x=380,y=200,width=900,height=500)
    
    bttn("label_apply_leave",frame_applyleave,0,0,2,56,"Apply For Leave",'green','lightgreen',"times new roman",20,"bold",None,None)

    #label_apply_leave=Label(frame_applyleave,text="Apply for Leave",font=("times new roman",20,"bold"),bg="light green",fg="black")
    #label_apply_leave.place(x=100,y=20)

    label_eid=Label(frame_applyleave,text="ID :",font=("arial",12,"bold"),bg="black",fg="white")
    label_eid.place(x=20,y=110)

    entry_eid=Entry(frame_applyleave,textvariable=var_eid,font=("times new roman",12,"bold"))
    entry_eid.place(x=180,y=110)

    label_name=Label(frame_applyleave,text="Name :",font=("arial",12,"bold"),bg="black",fg="white")
    label_name.place(x=20,y=170)

    entry_name=Entry(frame_applyleave,textvariable=var_name,font=("arial",12,"bold"))
    entry_name.place(x=180,y=170)
    
    label_department=Label(frame_applyleave,text="Department :",font=("arial",12,"bold"),bg="black",fg="white")
    label_department.place(x=440,y=110)

    entry_department=Entry(frame_applyleave,textvariable=var_department,font=("arial",12,"bold"))
    entry_department.place(x=600,y=110)
    
    label_cb1=Label(frame_applyleave,text="Leave Code :",font=("arial",12,"bold"),bg="black",fg="white")
    label_cb1.place(x=440,y=160)

    leavesgiven=['SL','CL','VL','Weekend','Other']
    cb1=ttk.Combobox(frame_applyleave,values=leavesgiven,width=10)
    cb1.place(x=600,y=160)

    label_noofdays=Label(frame_applyleave,text="No Of Days :",font=("arial",12,"bold"),bg="black",fg="white")
    label_noofdays.place(x=20,y=230)

    entry_noofdays=Entry(frame_applyleave,textvariable=var_noofdays,font=("arial",12,"bold"))
    entry_noofdays.place(x=180,y=230)
    
    
    label_fromcalander=Label(frame_applyleave,text="From date :",font=("arial",12,"bold"),bg="black",fg="white")
    label_fromcalander.place(x=20,y=290)
    
    cal1=DateEntry(frame_applyleave,textvariable=var_fromdate)
    cal1.place(x=180,y=290)

    
    label_tocalander=Label(frame_applyleave,text="To date :",font=("arial",12,"bold"),bg="black",fg="white")
    label_tocalander.place(x=20,y=350)
    
    cal2=DateEntry(frame_applyleave,textvariable=var_todate)
    cal2.place(x=180,y=350)

    
    label_reason=Label(frame_applyleave,text="Reason :",font=("arial",12,"bold"),bg="black",fg="white")
    label_reason.place(x=20,y=410)
    entry_reason=Entry(frame_applyleave, textvariable=var_reason ,font=("arial",12,"bold"))
    entry_reason.place(x=180,y=410,height=50,width=170)

    
    bttn("button_apply",frame_applyleave,450,250,2,16,"Apply",'light green','black',"forte",20,"bold",tabledata_from_applyleaveform,None)

    #button_apply=Button(frame_applyleave,command=tabledata_from_applyleaveform,text="Apply",bg="green")
    #button_apply.place(x=600,y=300,height=50,width=100)
    def btn_back():
        frame_applyleave.destroy()
    
    bttn("button_back",frame_applyleave,450,350,2,16,"Close Tab",'red','black',"forte",20,"bold",btn_back,None)

    #button_back=Button(frame_applyleave,text="Back",bg="green",command=btn_back)
    #button_back.place(x=600,y=400,height=50,width=100)
   #=======================================================================================================================
    
#=============================================================================================================================

bg2_page5=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\backtwo.jpg")
lbl_bg2_page5=Label(page5, image=bg2_page5)
lbl_bg2_page5.place(x=140, y=30, relwidth=1, relheight=1)
        #=====================frame=============================================



frame_lside_page5=Frame(page5, bg="black")
frame_lside_page5.place(x=0, y=0, relheight=1, width=300)

frame_top_page5=Frame(page5, bg="black")
frame_top_page5.place(x=0, y=0, height=150, width=1550)

        #frame1=Frame(self.root, bg="black")
        #frame1.place(x=125, y=200, height=600, width=1300)

bg1_page5=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\halk.png")
bg1_lbl_page5=Label(frame_top_page5,image=bg1_page5, bg="black",bd=10)
bg1_lbl_page5.place(x=590,y=0)

page5.tkraise()

frame_rside_page5=Frame(page5, bg="black")
frame_rside_page5.place(x=1500,y=0, relheight=1, width=40)

frame_bottom_page5=Frame(page5, bg="black")
frame_bottom_page5.place(x=0,y=770, relwidth=1, height=30)



        
        #==================headings and side text labels=============================================================

#lbl_hal_page5=Label(frame_top_page5, text=" Hindustan Aeronautics Limited", bg="lightgrey", fg="black", font=("Old English Text MT",30,"bold"))
#lbl_hal_page5.place(x=500, y=20)



#lbl_hal1=Label(frame_top_page5, text=" HAL", bg="lightgrey", fg="black", font=("Old English Text MT",30,"italic"))
#lbl_hal1.place(x=710, y=70)


        #========================buttons left frame===================================================

bttn("btn_applyleave",frame_lside_page5,1,200,3,19,"Apply Leave",'lightgreen','black',"forte",20,"bold",apply_leave,None)

#btn_applyleave=Button(frame_lside_page5, text="+ Apply Leave",command=apply_leave, fg="white", bg="blue", font=("arial",15,"bold"))
#btn_applyleave.place(x=70, y=250)

#bttn("lbl_Frame_page3",frame1_page3,0,11,1,19,"EMPLOYEE   LOGIN",'white','black',"Algerian",30,"bold",None,None)

bttn("btn_pending",frame_lside_page5,1,300,3,19,"Pending",'yellow','black',"forte",20,"bold",table_pending,None)

#btn_pending=Button(frame_lside_page5, text="Pending",command=table_pending, fg="white", bg="gold", font=("arial",15,"bold"))
#btn_pending.place(x=100, y=340)

bttn("btn_approve",frame_lside_page5,1,400,3,19,"Approve",'light blue','black',"forte",20,"bold",table_approved,None)

#btn_approve=Button(frame_lside_page5, text="Approved",command=table_approved, fg="white", bg="green", font=("arial",15,"bold"))
#btn_approve.place(x=90, y=430)

bttn("btn_rejected",frame_lside_page5,1,500,3,19,"Rejected",'pink','black',"forte",20,"bold",table_rejected,None)

bttn("btn_logout",frame_lside_page5,1,600,3,19,"Logout",'orange','black',"forte",20,"bold",logout,None)

#btn_logout=Button(frame_lside_page5, text="Logout",command=logout, fg="white", bg="red", font=("arial",13,"bold"))
#btn_logout.place(x=110, y=650)

bttn("btn_exit",frame_lside_page5,1,700,3,19,"Exit",'red','black',"forte",20,"bold",exit,None)

#btn_exit=Button(frame_lside_page5, text="Exit",command=exit, fg="white", bg="red", font=("arial",13,"bold"))
#btn_exit.place(x=120, y=700)

        #=============================FOOTER===================================================================
lbl_bottom=Label(frame_bottom_page5, text="All Rights Reserved @ Ayush Khare", bg="black", fg="white", font=("harlow solid italic",10,"bold"))
lbl_bottom.place(x=1200, y=25)

        #==============================logo user====================================================================
logo2_page5=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\employeelogo.png")
bg1_logo2_page5=Label(frame_top_page5,image=logo2_page5, bg="black",bd=10)
bg1_logo2_page5.place(x=100,y=40,height=90,width=90)

bttn("lbl_hal1",frame_lside_page5,70,150,1,19,"Employee",'white','black',"arial",10,"bold",None,None)

#lbl_userl_page5=Label(frame_top_page5, text="Employee", bg="lightgrey", fg="black", font=("ALGERIAN",15,"italic"))
#lbl_userl_page5.place(x=1380, y=120)




#============================================================================================================================
#============================================================================================================================
#============================================================================================================================

#============================================================================================================================
#============================================================================================================================
#===========================================PAGE 6===========================================================================
#============================================================================================================================
#============================================================================================================================

page6=Frame(win)
page6.place(x=0,y=0,relheight=1,relwidth=1)
#========================================================================================================================

#=========================================FUNCTIONS======================================================================

#=========================================LEAVE REQUESTS FUNCTION=======================================================
def leaverequests():
    frame=Frame(page6,bg="white")
    frame.place(x=380,y=200,width=900,height=500)
    
    frame_table=Frame(frame,bg="white")
    frame_table.place(x=0,y=0,width=900,height=400)


    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                     background="silver",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="grey"
                                )
    style.map('Treeview',background=[('selected','green')])
   

    scroll_x=ttk.Scrollbar(frame_table,orient="horizontal")
    scroll_y=ttk.Scrollbar(frame_table,orient="vertical")

    leave_table=ttk.Treeview(frame_table,column=("EID","name","department","noofdays","fromdate","todate","reason"),
    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x=ttk.Scrollbar(command=leave_table.xview)
    scroll_x=ttk.Scrollbar(command=leave_table.yview)


    leave_table.heading("EID",text="Employee ID")
    leave_table.heading("name",text="Name")
    leave_table.heading("department",text="Department")
    leave_table.heading("noofdays",text="Number Of Days")
    leave_table.heading("fromdate",text="From Date")
    leave_table.heading("todate",text="To Date")
    leave_table.heading("reason",text="Reason")
    

    leave_table["show"]="headings"

    leave_table.column("EID",width=100)
    leave_table.column("name",width=100)
    leave_table.column("department",width=100)
    leave_table.column("noofdays",width=100)
    leave_table.column("fromdate",width=100)
    leave_table.column("todate",width=100)
    leave_table.column("reason",width=100)
    
    leave_table.pack(fill=BOTH,expand=1)
    


    def approve():

        try:
            selected_item=leave_table.focus()
            details=leave_table.item(selected_item)
            selected_eid=details.get("values")[0]
            selected_fromdate=details.get("values")[4]
           
            messagebox.showinfo("success","success inselection")
        except:
            messagebox.showerror("error","error in selection")


        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
            my_cursor=conn.cursor()
            query='UPDATE leave_entry SET STATUS="APPROVED" WHERE EMPLOYEEID=%s AND FROM_DATE=%s'
            v=(selected_eid,selected_fromdate)
            my_cursor.execute(query,v)
            conn.commit()
            conn.close()
            messagebox.showinfo("success","success in query")
        except:
            messagebox.showerror("error","error in query")
        try:
            
            
            
            messagebox.showinfo("success","success")
            
        except:
            messagebox.showerror("error","error last")
               


    def rejected():

        try:
            selected_item=leave_table.focus()
            details=leave_table.item(selected_item)
            selected_eid=details.get("values")[0]
            selected_fromdate=details.get("values")[4]
           
            messagebox.showinfo("success","success inselection")
        except:
            messagebox.showerror("error","error in selection")


        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
            my_cursor=conn.cursor()
            query='UPDATE leave_entry SET STATUS="REJECTED" WHERE EMPLOYEEID=%s AND FROM_DATE=%s'
            v=(selected_eid,selected_fromdate)
            my_cursor.execute(query,v)
            conn.commit()
            conn.close()
            messagebox.showinfo("success","success in query")
        except:
            messagebox.showerror("error","error in query")
        try:
            
            
            
            messagebox.showinfo("success","success")
            
        except:
            messagebox.showerror("error","error last")

    bttn("b1",frame,0,400,3,19,"Approve",'lightblue','black',"forte",20,"bold",approve,None)
    
    #b1=Button(frame,command=approve,text="Approve",bg="green")
    #b1.place(x=150,y=450,height=50,width=50)
    
    bttn("b2",frame,300,400,3,19,"Reject",'pink','black',"forte",20,"bold",rejected,None)

    def btn_Close():
        frame.destroy()
        frame_table.destroy()
    
    bttn("b2",frame,600,400,3,19,"Close Tab",'red','black',"forte",20,"bold",btn_Close,None)

    #b2=Button(frame,command=rejected,text="Reject",bg="lightblue")
    #b2.place(x=250,y=450,height=50,width=50)

    conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
    my_cursor=conn.cursor()
    
    query="SELECT EMPLOYEEID,NAME,DEPARTMENT,NO_OF_DAYS,FROM_DATE,TO_DATE,REASON FROM EMPLOYEE,LEAVE_ENTRY WHERE EID=EMPLOYEEID AND STATUS='pending'"
    my_cursor.execute(query)
    try:
        rows=my_cursor.fetchall()
        for i in rows:
            leave_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("error","error")
    conn.commit()
    conn.close()
    
   

#=======================================================================================================================
#=======================================================================================================================

def logout():
    page2.tkraise()

def exit():
    page6.destroy()
    win.destroy()
#==========================================pending button function========================================================
def table_rejected_admin():
    frame=Frame(page6,bg="white")
    frame.place(x=380,y=200,width=900,height=500)

    frame_table=Frame(page6,bg="white")
    frame_table.place(x=380,y=200,width=900,height=400)

    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                     background="silver",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="grey"
                                )
    style.map('Treeview',background=[('selected','red')])

    scroll_x=ttk.Scrollbar(frame_table,orient="horizontal")
    scroll_y=ttk.Scrollbar(frame_table,orient="vertical")

    leave_table=ttk.Treeview(frame_table,column=("EID","name","department","noofdays","fromdate","todate","reason","status"),
    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x=ttk.Scrollbar(command=leave_table.xview)
    scroll_x=ttk.Scrollbar(command=leave_table.yview)


    leave_table.heading("EID",text="Employee ID")
    leave_table.heading("name",text="Name")
    leave_table.heading("department",text="Department")
    leave_table.heading("noofdays",text="Number Of Days")
    leave_table.heading("fromdate",text="From Date")
    leave_table.heading("todate",text="To Date")
    leave_table.heading("reason",text="Reason")
    leave_table.heading("status",text="Status")

    leave_table["show"]="headings"

    leave_table.column("EID",width=100)
    leave_table.column("name",width=100)
    leave_table.column("department",width=100)
    leave_table.column("noofdays",width=100)
    leave_table.column("fromdate",width=100)
    leave_table.column("todate",width=100)
    leave_table.column("reason",width=100)
    leave_table.column("status",width=100)
    leave_table.pack(fill=BOTH,expand=1)

    bttn("b1",frame,0,400,3,28,"Change Status",'lightblue','black',"forte",20,"bold",None,None)
    
    #b1=Button(frame,command=approve,text="Approve",bg="green")
    #b1.place(x=150,y=450,height=50,width=50)
    def btn_Close():
        frame.destroy()
        frame_table.destroy()
    
    bttn("b2",frame,450,400,3,28,"Close Tab",'pink','black',"forte",20,"bold",btn_Close,None)


    conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
    my_cursor=conn.cursor()
    
    query="SELECT EMPLOYEEID,NAME,DEPARTMENT,NO_OF_DAYS,FROM_DATE,TO_DATE,REASON,STATUS FROM EMPLOYEE,LEAVE_ENTRY WHERE EID=EMPLOYEEID AND STATUS='Rejected'"
    my_cursor.execute(query)
    try:
        rows=my_cursor.fetchall()
        for i in rows:
            leave_table.insert("",END,values=i)
            b1=Button(leave_table,text="approve")
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("error","error")





#===========================================================================================================================
#==============================================approved button function=====================================================

def table_approved_admin():

    frame=Frame(page6,bg="white")
    frame.place(x=380,y=200,width=900,height=500)

    frame_table=Frame(page6,bg="white")
    frame_table.place(x=380,y=200,width=900,height=400)

    style=ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                     background="silver",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="grey"
                                )
    style.map('Treeview',background=[('selected','lightblue')])

    scroll_x=ttk.Scrollbar(frame_table,orient="horizontal")
    scroll_y=ttk.Scrollbar(frame_table,orient="vertical")

    leave_table=ttk.Treeview(frame_table,column=("EID","name","department","noofdays","fromdate","todate","reason","status"),
    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x=ttk.Scrollbar(command=leave_table.xview)
    scroll_x=ttk.Scrollbar(command=leave_table.yview)


    leave_table.heading("EID",text="Employee ID")
    leave_table.heading("name",text="Name")
    leave_table.heading("department",text="Department")
    leave_table.heading("noofdays",text="Number Of Days")
    leave_table.heading("fromdate",text="From Date")
    leave_table.heading("todate",text="To Date")
    leave_table.heading("reason",text="Reason")
    leave_table.heading("status",text="Status")

    leave_table["show"]="headings"

    leave_table.column("EID",width=100)
    leave_table.column("name",width=100)
    leave_table.column("department",width=100)
    leave_table.column("noofdays",width=100)
    leave_table.column("fromdate",width=100)
    leave_table.column("todate",width=100)
    leave_table.column("reason",width=100)
    leave_table.column("status",width=100)
    leave_table.pack(fill=BOTH,expand=1)

    bttn("b1",frame,0,400,3,28,"Change Status",'lightblue','black',"forte",20,"bold",None,None)
    
    def btn_Close():
        frame.destroy()
        frame_table.destroy()
    
    bttn("b2",frame,450,400,3,28,"Close Tab",'pink','black',"forte",20,"bold",btn_Close,None)
    
    conn=mysql.connector.connect(host="localhost",user="root",password="ayush120303",database="leavemanagement")
    my_cursor=conn.cursor()
    
    query="SELECT EMPLOYEEID,NAME,DEPARTMENT,NO_OF_DAYS,FROM_DATE,TO_DATE,REASON,STATUS FROM EMPLOYEE,LEAVE_ENTRY WHERE EID=EMPLOYEEID AND STATUS='approved'"
    my_cursor.execute(query)
    try:
        rows=my_cursor.fetchall()
        for i in rows:
            leave_table.insert("",END,values=i)
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("error","error")

#========================================================================================================================
#========================================================================================================================
#bg2_page6=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\pexels-cristian-benavides-2665150.jpg")
#lbl_bg2_page6=Label(page6, image=bg2_page6)
#lbl_bg2_page6.place(x=0, y=0, relwidth=1, relheight=1)

bg2_page6=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\backtwo.jpg")
lbl_bg2_page6=Label(page6, image=bg2_page6)
lbl_bg2_page6.place(x=140, y=30, relwidth=1, relheight=1)
#=====================frame=============================================

frame_lside_page6=Frame(page6, bg="black")
frame_lside_page6.place(x=0, y=0, relheight=1, width=300)

frame_top_page6=Frame(page6, bg="black")
frame_top_page6.place(x=0, y=0, height=150, width=1550)

        #frame1=Frame(self.root, bg="black")
        #frame1.place(x=125, y=200, height=600, width=1300)

#bg1_page6=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\haln.jpg")
#bg1_lbl_page6=Label(page6,image=bg1_page6, bg="white",bd=10)
#bg1_lbl_page6.place(x=50,y=20,height=139,width=200)

bg1_page6=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\halk.png")
bg1_lbl_page5=Label(frame_top_page6,image=bg1_page6, bg="black",bd=10)
bg1_lbl_page5.place(x=590,y=0)

frame_rside_page6=Frame(page6, bg="black")
frame_rside_page6.place( x=1500,y=0, relheight=1, width=40)

frame_bottom_page6=Frame(page6, bg="black")
frame_bottom_page6.place( x=0,y=770, relwidth=1, height=30)

        
        #==================headings and side text labels=============================================================

#lbl_hal_page6=Label(frame_top_page6, text=" Hindustan Aeronautics Limited", bg="lightgrey", fg="black", font=("Old English Text MT",30,"bold"))
#lbl_hal_page6.place(x=500, y=20)

#lbl_hal1_page6=Label(frame_top_page6, text=" HAL", bg="lightgrey", fg="black", font=("Old English Text MT",30,"italic"))
#lbl_hal1_page6.place(x=710, y=70)

        #========================buttons left frame===================================================

#bttn("btn_applyleave",frame_lside_page5,1,200,3,19,"Apply Leave",'lightgreen','black',"forte",20,"bold",apply_leave,None)

#btn_applyleave=Button(frame_lside_page5, text="+ Apply Leave",command=apply_leave, fg="white", bg="blue", font=("arial",15,"bold"))
#btn_applyleave.place(x=70, y=250)

#bttn("lbl_Frame_page3",frame1_page3,0,11,1,19,"EMPLOYEE   LOGIN",'white','black',"Algerian",30,"bold",None,None)

#bttn("btn_pending",frame_lside_page5,1,300,3,19,"Pending",'yellow','black',"forte",20,"bold",table_pending,None)

#btn_pending=Button(frame_lside_page5, text="Pending",command=table_pending, fg="white", bg="gold", font=("arial",15,"bold"))
#btn_pending.place(x=100, y=340)

#bttn("btn_approve",frame_lside_page5,1,400,3,19,"Approve",'light blue','black',"forte",20,"bold",table_approved,None)

#btn_approve=Button(frame_lside_page5, text="Approved",command=table_approved, fg="white", bg="green", font=("arial",15,"bold"))
#btn_approve.place(x=90, y=430)

#bttn("btn_logout",frame_lside_page5,1,500,3,19,"Logout",'orange','black',"forte",20,"bold",logout,None)

#btn_logout=Button(frame_lside_page5, text="Logout",command=logout, fg="white", bg="red", font=("arial",13,"bold"))
#btn_logout.place(x=110, y=650)

#bttn("btn_exit",frame_lside_page5,1,600,3,19,"Exit",'red','black',"forte",20,"bold",exit,None)

#btn_exit=Button(frame_lside_page5, text="Exit",command=exit, fg="white", bg="red", font=("arial",13,"bold"))
#btn_exit.place(x=120, y=700)      

        #========================buttons left frame===================================================
        


#btn_approve_page6=Button(frame_lside_page6, text="Profile", fg="white", bg="green", font=("arial",15,"bold"))
#btn_approve_page6.place(x=90, y=300)

bttn("btn_applyleave",frame_lside_page6,1,200,3,19,"Leave Requests",'orange','black',"forte",20,"bold",leaverequests,None)

#btn_applyleave_page6=Button(frame_lside_page6,command=leaverequests, text="Leave Requests", fg="white", bg="blue", font=("arial",15,"bold"))
#btn_applyleave_page6.place(x=70, y=400)

bttn("btn_pending_page6",frame_lside_page6,1,300,3,19,"Rejected",'pink','black',"forte",20,"bold",table_rejected_admin,None)      

#btn_pending_page6=Button(frame_lside_page6,command=table_rejected_admin, text="Rejected", fg="white", bg="gold", font=("arial",15,"bold"))
#btn_pending_page6.place(x=100, y=460)

bttn("btn_approve_page6",frame_lside_page6,1,400,3,19,"Approved",'light blue','black',"forte",20,"bold",table_approved_admin,None)

#btn_approve_page6=Button(frame_lside_page6,command=table_approved_admin, text="Approved", fg="white", bg="green", font=("arial",15,"bold"))
#btn_approve_page6.place(x=90, y=520)

bttn("btn_logout_page6",frame_lside_page6,1,500,3,19,"Logout",'orange','black',"forte",20,"bold",logout,None)

#btn_logout_page6=Button(frame_lside_page6, command=logout,text="Logout", fg="white", bg="red", font=("arial",13,"bold"))
#btn_logout_page6.place(x=110, y=650)

bttn("btn_exit_page6",frame_lside_page6,1,600,3,19,"Exit",'red','black',"forte",20,"bold",exit,None)

#btn_logout_page6=Button(frame_lside_page6,command=exit, text="Exit", fg="white", bg="red", font=("arial",13,"bold"))
#btn_logout_page6.place(x=120, y=700)

        #=============================FOOTER===================================================================
lbl_bottom_page6=Label(frame_bottom_page6, text="All Rights Reserved @ Ayush Khare", bg="lightgrey", fg="black", font=("harlow solid italic",10,"bold"))
lbl_bottom_page6.place(x=1200, y=25)

        #==============================logo user====================================================================
#logo2_page6=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\logoa.png")
#bg1_logo2_page6=Label(frame_top_page6,image=logo2_page6, bg="white",bd=10)
#bg1_logo2_page6.place(x=1390,y=20,height=90,width=90)

#lbl_userl_page6=Label(frame_top_page6, text="Admin", bg="lightgrey", fg="black", font=("arial",15,"italic"))
#lbl_userl_page6.place(x=1400, y=120)

logo2_page6=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\adminlogo.png")
bg1_logo2_page6=Label(frame_top_page6,image=logo2_page6, bg="black",bd=10)
bg1_logo2_page6.place(x=90,y=30,height=100,width=100)

bttn("lbl_admin_page6",frame_lside_page6,70,150,1,19,"Admin",'white','black',"arial",10,"bold",None,None)


#============================================================================================================================
#============================================================================================================================
#============================================================================================================================
#============================================================================================================================
page1.tkraise()
win.geometry("1540x800+0+0")
win.title("Leave Management System")

win.mainloop()






