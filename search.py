from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk
import mysql.connector as sql
def searching():
      #root= Tk()
      smenu = Toplevel()
      smenu.title("Update")
      smenu.resizable(False,False)
      smenu.geometry("800x520+300+20")
      bg= ImageTk.PhotoImage(file="delete.jpg")
      back= Label(smenu, image=bg).place(x=0,y=0)
      p1 = ImageTk.PhotoImage(file = 'search.png')
      smenu.iconphoto(False, p1)
      mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
      cursor=mycon.cursor()
      lab= Label(smenu, text="  SEARCH  ", font=("agency fb",35,"bold"), relief=RIDGE, bd=7,bg="white",fg="black")
      lab.place(x=300,y=10)
      ent1= Entry(smenu, bd=5, width=16, font=("agency fb",29))
      ent1.place(x=30,y=130)

      #======================canvas===========================================================================
      canva2 = LabelFrame(smenu,bd=10, bg="white",relief=RIDGE,font=("agency fb",25,"bold"),text="User Data")
      canva2.place(x=425,y=90,height=415, width=325)
      #================================table=============================================================
      canva = LabelFrame(smenu,bd=10, bg="lime",relief=RIDGE)
      canva.place(x=25,y=220,height=140)
      style  = ttk.Style()
      style.configure("Treeview.Heading", font=("agency fb",16,"bold"))
      tree = ttk.Treeview(canva)
      tree["columns"] = ("fn", "ln","empno")
      tree.column("fn", width=120)
      tree.column("ln", width=120)
      tree.column("empno", width=60)
      tree.heading("#0", text='ID')
      tree.column("#0", width=30)
      tree.heading("fn", text="First Name")
      tree.heading("ln", text="Last Name")
      tree.heading("empno", text="Emp.No")
      cursor.execute("select * from emp;")
      l = cursor.fetchall()
      cpt = 0
      for r in l:
            tree.insert('', 'end', text=str(cpt), values=(r[0],r[1], r[5]))
            cpt += 1
      tree.pack()
      #===============================================================================================        
      def exitwin():
          win= Tk()
          win.geometry("250x90+540+320")
          win.title("Warning!")
          def adios():
               smenu.destroy()
               win.destroy()
          def na():
               win.destroy()

          lab= Label(win, text="Do you want", font=("consolas",12,"bold")).pack()
          lab= Label(win, text="to Exit the Table", font=("consolas",12,"bold")).pack()
          but1= Button(win, text="Yes", fg="white",command=adios,bg="sky blue",font=("agency fb",14,"bold"),padx=47)
          but1.pack(side=LEFT)
          but2= Button(win, text="No", fg="white", bg="Red",command=na,font=("agency fb",14,"bold"),padx=50)
          but2.pack(side=LEFT)
          smenu.bind('<y>',lambda event:adios())
          smenu.bind('<n>',lambda event:na())
      #=================================================================================================================
      def showdata():
            import tkinter as tk
            import mysql.connector as sql
            mycon= sql.connect(host="localhost", user="root", password="tiger", database="test")
            cursor=mycon.cursor()
            getnum=ent1.get()
            s="select * from emp where enpno='{}';".format(getnum)
            cursor.execute(s)
            f=cursor.fetchall()
            for row in f:
                  name=row[0]+" "+row[1]
                  emailget=row[2]
                  getphone=row[3]
                  ageget=row[4]
                  empnoget=row[5]
                  salaryget=row[6]
                  dobget=row[7]
                  qual=row[8]
                  desigget=row[9]

                  l1= Label(canva2,bg="white",text=name, font=("agency fb",20,"bold"), padx=10)
                  l1.grid(row=0,column=1)
                  l2= Label(canva2,bg="white",text=emailget, font=("agency fb",20,"bold"), padx=10)
                  l2.grid(row=2,column=1)
                  l3= Label(canva2,bg="white",text=getphone, font=("agency fb",20,"bold"), padx=10)
                  l3.grid(row=3,column=1)
                  l4= Label(canva2,bg="white",text=ageget, font=("agency fb",20,"bold"), padx=10)
                  l4.grid(row=4,column=1)
                  l5= Label(canva2,bg="white",text=empnoget, font=("agency fb",20,"bold"), padx=10)
                  l5.grid(row=5,column=1)
                  l6= Label(canva2,bg="white",text=salaryget, font=("agency fb",20,"bold"), padx=10)
                  l6.grid(row=6,column=1)
                  l7= Label(canva2,bg="white",text=dobget, font=("agency fb",20,"bold"), padx=10)
                  l7.grid(row=7,column=1)
                  l8= Label(canva2,bg="white",text=qual, font=("agency fb",20,"bold"), padx=10)
                  l8.grid(row=8,column=1)
                  l9= Label(canva2,bg="white",text=desigget, font=("agency fb",20,"bold"), padx=10)
                  l9.grid(row=9,column=1)

      #==============================================================================================================================

      l1= Label(canva2,bg="white",text="Name :", font=("agency fb",20,"bold"), padx=10)
      l1.grid(row=0,column=0)
      l2= Label(canva2,bg="white",text="Email :", font=("agency fb",20,"bold"), padx=10)
      l2.grid(row=2,column=0)
      l3= Label(canva2,bg="white",text="Phone :", font=("agency fb",20,"bold"), padx=10)
      l3.grid(row=3,column=0)
      l4= Label(canva2,bg="white",text="Age :", font=("agency fb",20,"bold"), padx=10)
      l4.grid(row=4,column=0)
      l5= Label(canva2,bg="white",text="Employee No :", font=("agency fb",20,"bold"), padx=10)
      l5.grid(row=5,column=0)
      l6= Label(canva2,bg="white",text="Salary :", font=("agency fb",20,"bold"), padx=10)
      l6.grid(row=6,column=0)
      l7= Label(canva2,bg="white",text="DOB :", font=("agency fb",20,"bold"), padx=10)
      l7.grid(row=7,column=0)
      l8= Label(canva2,bg="white",text="Qualification :", font=("agency fb",20,"bold"), padx=10)
      l8.grid(row=8,column=0)
      l9= Label(canva2,bg="white",text="Designation :", font=("agency fb",20,"bold"), padx=10)
      l9.grid(row=9,column=0)
      #==============================================================================================================================
      but2= Button(smenu, text="O",font=("",20,"bold"), bd=5,command=showdata)
      but2.place(x=320,y=129, height=58,width=60)
      btn3= Button(smenu, bd=5, fg="red",text="EXIT",command=exitwin ,font=("agency fb",22,"bold"),padx=20, pady=1)
      btn3.place(x=20,y=430,height=56)
      smenu.bind('<Escape>',lambda event:exitwin())
      #smenu.bind('<Return>',lambda event:on_button())
      smenu.mainloop()
