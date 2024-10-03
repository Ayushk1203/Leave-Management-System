from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import random
import time
import datetime
from tkcalendar import *
from tkinter import messagebox
import mysql.connector

from time import strftime




win=tk.Tk()
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
#============================================================================================================================
#============================================PAGE5===========================================================================
#============================================================================================================================
#============================================================================================================================

page5=Frame(win)
page5.place(x=0,y=0,relheight=1,relwidth=1)

#===========================================Functions========================================================================


#==========================================pending button function========================================================
def table_pending():
    frame_table=Frame(page5,bg="white")
    frame_table.place(x=380,y=200,width=900,height=500)
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
    frame_table=Frame(page5,bg="white")
    frame_table.place(x=380,y=200,width=900,height=500)
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
    frame_applyleave=Frame(page5,bg="white")
    frame_applyleave.place(x=380,y=200,width=700,height=500)

    label_apply_leave=Label(frame_applyleave,text="Fill the details below to Apply for Leave",font=("times new roman",20,"bold"))
    label_apply_leave.place(x=20,y=20)

    label_eid=Label(frame_applyleave,text="Employee ID :",font=("arial",15,"bold"))
    label_eid.place(x=20,y=80)

    entry_eid=Entry(frame_applyleave,textvariable=var_eid,font=("times new roman",12,"bold"))
    entry_eid.place(x=180,y=80)

    label_name=Label(frame_applyleave,text="Name :",font=("arial",15,"bold"))
    label_name.place(x=20,y=140)

    entry_name=Entry(frame_applyleave,textvariable=var_name,font=("arial",12,"bold"))
    entry_name.place(x=180,y=140)
    
    label_department=Label(frame_applyleave,text="Department :",font=("arial",15,"bold"))
    label_department.place(x=400,y=100)

    entry_department=Entry(frame_applyleave,textvariable=var_department,font=("arial",12,"bold"))
    entry_department.place(x=450,y=140)

    label_noofdays=Label(frame_applyleave,text="No Of Days :",font=("arial",15,"bold"))
    label_noofdays.place(x=20,y=200)

    entry_noofdays=Entry(frame_applyleave,textvariable=var_noofdays,font=("arial",15,"bold"))
    entry_noofdays.place(x=180,y=200)
    
    
    label_fromcalander=Label(frame_applyleave,text="From date :",font=("arial",15,"bold"))
    label_fromcalander.place(x=20,y=260)
    
    cal1=DateEntry(frame_applyleave,textvariable=var_fromdate)
    cal1.place(x=180,y=260)

    
    label_tocalander=Label(frame_applyleave,text="To date :",font=("arial",15,"bold"))
    label_tocalander.place(x=20,y=320)
    
    cal2=DateEntry(frame_applyleave,textvariable=var_todate)
    cal2.place(x=180,y=320)

    
    label_reason=Label(frame_applyleave,text="Reason :",font=("arial",15,"bold"))
    label_reason.place(x=20,y=380)
    entry_reason=Entry(frame_applyleave, textvariable=var_reason ,font=("arial",15,"bold"))
    entry_reason.place(x=180,y=380,height=100,width=100)


    button_apply=Button(frame_applyleave,command=tabledata_from_applyleaveform,text="Apply",bg="green")
    button_apply.place(x=500,y=300,height=50,width=100)
    def btn_back():
        frame_applyleave.destroy()

    button_back=Button(frame_applyleave,text="Back",bg="green",command=btn_back)
    button_back.place(x=500,y=400,height=50,width=100)
   #=======================================================================================================================
    
#=============================================================================================================================

bg2_page5=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\pexels-cristian-benavides-2665150.jpg")
lbl_bg2_page5=Label(page5, image=bg2_page5)
lbl_bg2_page5.place(x=0, y=0, relwidth=1, relheight=1)
        #=====================frame=============================================

frame_lside_page5=Frame(page5, bg="lightgrey")
frame_lside_page5.place(x=0, y=0, relheight=1, width=300)

frame_top_page5=Frame(page5, bg="lightgrey")
frame_top_page5.place(x=0, y=0, height=150, width=1550)

        #frame1=Frame(self.root, bg="black")
        #frame1.place(x=125, y=200, height=600, width=1300)

bg1_page5=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\haln.jpg")
bg1_lbl_page5=Label(page5,image=bg1_page5, bg="white",bd=10)
bg1_lbl_page5.place(x=50,y=20,height=139,width=200)

frame_rside_page5=Frame(page5, bg="lightgrey")
frame_rside_page5.place( x=1500,y=0, relheight=1, width=40)

frame_bottom_page5=Frame(page5, bg="lightgrey")
frame_bottom_page5.place( x=0,y=740, relwidth=1, height=60)

        
        #==================headings and side text labels=============================================================

lbl_hal_page5=Label(frame_top_page5, text=" Hindustan Aeronautics Limited", bg="lightgrey", fg="black", font=("Old English Text MT",30,"bold"))
lbl_hal_page5.place(x=500, y=20)

lbl_hal1=Label(frame_top_page5, text=" HAL", bg="lightgrey", fg="black", font=("Old English Text MT",30,"italic"))
lbl_hal1.place(x=710, y=70)


        #========================buttons left frame===================================================

btn_applyleave=Button(frame_lside_page5, text="+ Apply Leave",command=apply_leave, fg="white", bg="blue", font=("arial",15,"bold"))
btn_applyleave.place(x=70, y=250)

btn_pending=Button(frame_lside_page5, text="Pending",command=table_pending, fg="white", bg="gold", font=("arial",15,"bold"))
btn_pending.place(x=100, y=340)

btn_approve=Button(frame_lside_page5, text="Approved",command=table_approved, fg="white", bg="green", font=("arial",15,"bold"))
btn_approve.place(x=90, y=430)

btn_logout=Button(frame_lside_page5, text="Logout", fg="white", bg="red", font=("arial",13,"bold"))
btn_logout.place(x=110, y=650)

btn_logout=Button(frame_lside_page5, text="Exit", fg="white", bg="red", font=("arial",13,"bold"))
btn_logout.place(x=120, y=700)

        #=============================FOOTER===================================================================
lbl_bottom=Label(frame_bottom_page5, text="All Rights Reserved @ Ayush Khare", bg="lightgrey", fg="black", font=("harlow solid italic",10,"bold"))
lbl_bottom.place(x=1200, y=25)

        #==============================logo user====================================================================
logo2_page5=ImageTk.PhotoImage(file=r"D:\Vocational Training project\images\resized\logou.png")
bg1_logo2_page5=Label(frame_top_page5,image=logo2_page5, bg="white",bd=10)
bg1_logo2_page5.place(x=1390,y=20,height=90,width=90)

lbl_userl_page5=Label(frame_top_page5, text="Employee", bg="lightgrey", fg="black", font=("ALGERIAN",15,"italic"))
lbl_userl_page5.place(x=1380, y=120)



win.geometry("1540x800+0+0")
win.title("Leave Management System")

win.mainloop()

'''var_cal3=StringVar()
    var_cal4=StringVar()

    def no_of_days():
        noofdays=var_cal4-var_cal3
        label_nod=Label(frame_applyleave,text=noofdays,fg="black",font=("arial",100,"bold"))
        label_nod.place(x=300,y=200,height=100,width=100)
    
    def get_date():

        frame=Frame(frame_applyleave)
        frame.place(x=200,y=200,height=280,width=240)
        
        cal=Calendar(frame)
        cal.place(x=0,y=0,height=240,width=240)

        def print_date():
            dt=cal.get_date()
            var_cal3=dt
            
            l1=Label(frame_applyleave,text=dt)
            l1.place(x=160,y=190,height=50,width=50)
            frame.destroy()

        button_submit=Button(frame,text="submit",command=print_date)
        button_submit.place(x=100,y=240,height=40,width=40)



    button_getdate=Button(frame_applyleave,text="select date",command=get_date)
    button_getdate.place(x=200,y=200,height=40,width=100)
    #==============================================================================
    #==================================TO DATE ====================================
    label_calander=Label(frame_applyleave,text="TO date :",font=("arial",10,"bold"))
    label_calander.place(x=20,y=300)
    
    def get_date():
        frame1=Frame(frame_applyleave)
        frame1.place(x=300,y=200,height=280,width=240)

        cal1=Calendar(frame1)
        cal1.place(x=0,y=0,height=240,width=240)

        

        def print_date():
            cal1.config()
            dt1=cal1.get_date()
            
            
            var_cal4=dt1
            l2=Label(frame_applyleave,text=dt1)
            l2.place(x=260,y=290,height=50,width=50)
            frame1.destroy()

        button_submit2=Button(frame1,text="submit",command=print_date)
        button_submit2.place(x=100,y=240,height=40,width=40)



    button_getdate1=Button(frame_applyleave,text="select date",command=get_date)
    button_getdate1.place(x=200,y=300,height=40,width=100)






    label_reason=Label(frame_applyleave,text="No Of Days :",font=("arial",10,"bold"))
    label_reason.place(x=20,y=240)

    button_nod1=Button(frame_applyleave,text="get days",bg="green",command=no_of_days)
    button_nod1.place(x=500,y=450,height=50,width=100)'''