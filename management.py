from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
#import mysql.connector
#def hello():

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Database Management")
        self.root.geometry("1530x800+0+0")
        #bg= PhotoImage(file="kf.png")
        #lab= Label(root, image=bg)
        #bg="lime",lab.place(x=0, y=0)

        firstLabel= Label(self.root, bd=20, relief= RIDGE, text="EMPLOYEE MANAGEMENT DATABASE", fg="green", bg="white", font=("consolas",30,"bold"))
        firstLabel.pack(side=TOP, fill=X)

        self.labelnamefname = StringVar()
        self.labelnamelname = StringVar()
        self.labelphone = StringVar()
        self.labelempno = StringVar()
        self.labeldesig = StringVar()
        self.labelemail = StringVar()
        self.labeladdress = StringVar()
        self.labelsalary = StringVar()
        self.labelage = StringVar()
        self.labeldob = StringVar()
        self.labeljoindate = StringVar()
        self.labelqualifications = StringVar()
        self.labelschedule = StringVar()

        #============================DATAFRAME===================================================================
        dataframe= Frame(self.root, bd=20, relief=RIDGE)
        dataframe.place(x=0, y=90, width=1370, height=400)

        dataframeleft= LabelFrame(dataframe, bd=10, relief=RIDGE, padx=10,
                                  font=('consolas',13,'bold'), text="Employee Information")
        dataframeleft.place(x=0, y=5, width=980, height=350)
        dataframeright= LabelFrame(dataframe, bd=10, relief=RIDGE, padx=10,
                                  font=('consolas',13,'bold'), text="Prescription")
        dataframeright.place(x=984, y=5, width=345, height=350)

#========================buttomns=======================================================

        buttonframe= Frame(self.root, bd=13, relief=RIDGE)
        buttonframe.place(x=0, y=486, width=1360, height=70)

#======================details ==========================================================
        detailsframe= Frame(self.root, bd=20, relief=RIDGE)
        detailsframe.place(x=0, y=554, width=1360, height=170)

#===========================detailframeleft===============================================

        labelnamefname= Label(dataframeleft, font=("consolas",13,"bold"), text="First Name",padx=2, pady=8)
        labelnamefname.grid(row=0, column=0, sticky=W)
        entrynamefname= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelnamefname, width=32, bd=2)
        entrynamefname.grid(row=0, column=1)

        labelnamelname= Label(dataframeleft, font=("consolas",13,"bold"), text="Last Name",padx=2, pady=8)
        labelnamelname.grid(row=1, column=0, sticky=W)
        entrynamelname= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelnamelname, width=32, bd=2)
        entrynamelname.grid(row=1, column=1)

        labelemail= Label(dataframeleft, font=("consolas",13,"bold"), text="Email-ID",padx=2, pady=8)
        labelemail.grid(row=2, column=0, sticky=W)
        labelemail= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelemail, width=32, bd=2)
        labelemail.grid(row=2, column=1)

        labelphone= Label(dataframeleft, font=("consolas",13,"bold"), text="Phone",padx=2, pady=8)
        labelphone.grid(row=3, column=0, sticky=W)
        entryphone= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelphone, width=32, bd=2)
        entryphone.grid(row=3, column=1)

        labelage= Label(dataframeleft, font=("consolas",13,"bold"), text="Age",padx=2, pady=8)
        labelage.grid(row=4, column=0, sticky=W)
        entryage= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelage, width=32, bd=2)
        entryage.grid(row=4, column=1)

        labelempno= Label(dataframeleft, font=("consolas",13,"bold"), text="Employee No.",padx=2, pady=8)
        labelempno.grid(row=5, column=0, sticky=W)
        entryempno= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelempno, width=32, bd=2)
        entryempno.grid(row=5, column=1)
        buttonx= Button(dataframeleft, text="NEW",width=8, font=("consolas",10,"bold")).grid(row=5, column=3, sticky=W)

        labelsalary= Label(dataframeleft, font=("consolas",13,"bold"), text="Salary",padx=2, pady=8)
        labelsalary.grid(row=6, column=0, sticky=W)
        entrysalary= Entry(dataframeleft, font=("consolas",13,"bold"),textvariable=self.labelsalary, width=32, bd=2)
        entrysalary.grid(row=6, column=1)
#==================================right==============================================


        labeldob = Label(dataframeleft, text="DOB", font=('consolas',13, "bold"), textvariable=self.labeldob,padx=15, pady=8)
        labeldob.grid(row=0, column=3, sticky=W)
        labeldob = ttk.Combobox(dataframeleft, font=("consolas",13, "bold"), width=30)
        labeldob["values"] = ("Junior Employee", "Senior Employee", "Junior Manager")
        labeldob.grid(row=0, column=4)

        labeljoindate = Label(dataframeleft, font=("consolas",13, "bold"), text="Joining Date", padx=15, pady=8)
        labeljoindate.grid(row=1, column=3, sticky=W)
        entryjoindate = Entry(dataframeleft, font=("consolas",13, "bold"),textvariable=self.labeljoindate, width=32, bd=2)
        entryjoindate.grid(row=1, column=4)

        labelqualifications = Label(dataframeleft, font=("consolas",13, "bold"), text="Qualification", padx=15, pady=8)
        labelqualifications.grid(row=2, column=3, sticky=W)
        entryqualifications = Entry(dataframeleft, font=("consolas",13, "bold"),textvariable=self.labelqualifications, width=32, bd=2)
        entryqualifications.grid(row=2, column=4)

        labeldesig = Label(dataframeleft, font=("consolas",13, "bold"), text="Designation", padx=15, pady=8)
        labeldesig.grid(row=3, column=3, sticky=W)
        entrydesig = Entry(dataframeleft, font=("consolas",13, "bold"),textvariable=self.labeldesig, width=32, bd=2)
        entrydesig.grid(row=3, column=4)

        labelschedule = Label(dataframeleft, font=("consolas",13, "bold"), text="Schedule", padx=15, pady=8)
        labelschedule.grid(row=4, column=3, sticky=W)
        entryschedule = Entry(dataframeleft, font=("consolas",13, "bold"),textvariable=self.labelschedule, width=32, bd=2)
        entryschedule.grid(row=4, column=4)

        labeladdress = Label(dataframeleft, font=("consolas",13, "bold"), text="Address", padx=15, pady=8)
        labeladdress.grid(row=6, column=3, sticky=W)
        entryaddress = Text(dataframeleft, font=("consolas",13, "bold"), width=32, height=3, bd=3)
        entryaddress.grid(row=6, column=4)

#========================================Dataframeright======================================================================
        self.txtPrescripion= Text(dataframeright, font=("consolas",13,"bold"), width=34, height=15, padx=0, pady=2)
        self.txtPrescripion.grid(row=0, column=0)

#===============================================BUTTONS====================================================================
        button1= Button(buttonframe, text="Prescription", font=("consolas",13,"bold"),bg="lime", width=24, height=1, padx=2, pady=6)
        button1.grid(row=0, column=0)

        button1= Button(buttonframe, text="Prescription Data", font=("consolas",13,"bold"),bg="lime", width=23, height=1, padx=2, pady=6)
        button1.grid(row=0, column=1)

        button1= Button(buttonframe, text="Update", font=("consolas",13,"bold"),bg="lime", width=24, height=1, padx=2, pady=6)
        button1.grid(row=0, column=2)

        button1= Button(buttonframe, text="Delete", font=("consolas",13,"bold"),bg="lime", width=23, height=1, padx=2, pady=6)
        button1.grid(row=0, column=3)

        button1= Button(buttonframe, text="Clear", font=("consolas",13,"bold"),bg="lime", width=23, height=1, padx=2, pady=6)
        button1.grid(row=0, column=4)

        button1= Button(buttonframe, text="Exit", font=("consolas",13,"bold"),bg="lime", width=23, height=1, padx=2, pady=6)
        button1.grid(row=0, column=5)

#=====================================scrollbar=====================================================================================
        scroll_x= ttk.Scrollbar(detailsframe, orient= HORIZONTAL)
        scroll_y= ttk.Scrollbar(detailsframe, orient= VERTICAL)
        self.employee_table= ttk.Treeview(detailsframe, column=("labelnamefname","labelnamelname","labelphone","labelempno","labeldesig",
                                                                "labelemail","labeladdress","labelsalary","labelage","labeldob","labeljoindate",
                                                                "labelqualifications","labelschedule")
                                          ,xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x= ttk.Scrollbar(command=self.employee_table.xview)
        scroll_y= ttk.Scrollbar(command=self.employee_table.yview)

        self.employee_table.heading("labelnamefname",text="FNAME")
        self.employee_table.heading("labelnamelname",text="LNAME")
        self.employee_table.heading("labelphone",text="PHONE")
        self.employee_table.heading("labelempno",text="Employee Number")
        self.employee_table.heading("labeldesig",text="Designation")
        self.employee_table.heading("labelemail",text="Email")
        self.employee_table.heading("labeladdress",text="Address")
        self.employee_table.heading("labelsalary",text="Salary")
        self.employee_table.heading("labelage",text="Age")
        self.employee_table.heading("labeldob",text="DOB")
        self.employee_table.heading("labeljoindate",text="Joining Date")
        self.employee_table.heading("labelqualifications",text="Qualifications")
        self.employee_table.heading("labelschedule",text="Timings")

        self.employee_table["show"]="headings"

        self.employee_table.column("labelnamefname", width=100)
        self.employee_table.column("labelnamelname", width=100)
        self.employee_table.column("labelphone", width=100)
        self.employee_table.column("labelempno", width=100)
        self.employee_table.column("labeldesig", width=100)
        self.employee_table.column("labelemail", width=100)
        self.employee_table.column("labeladdress", width=100)
        self.employee_table.column("labelsalary", width=100)
        self.employee_table.column("labelage", width=100)
        self.employee_table.column("labeldob", width=100)
        self.employee_table.column("labeljoindate", width=100)
        self.employee_table.column("labelqualifications", width=100)
        self.employee_table.column("labelschedule", width=100)

        self.employee_table.pack(fill=BOTH, expand=1)




root= Tk()
ob= Employee(root)
root.mainloop()










