from tkinter import *
from PIL import ImageTk
from spare2 import hello
from delete import dele
from search import searching
from show_data import show
def man():
    menu = Toplevel()
    menu.title("Management")
    menu.geometry("740x500")
    p1 = ImageTk.PhotoImage(file = 'menu.png')
    menu.iconphoto(False, p1)        
    menu['background'] = 'white'
    menu.resizable(False,False)
    def exitwin():
        win= Tk()
        win.geometry("250x90+540+320")
        win.title("Warning!")
        def adios():
             menu.destroy()
             win.destroy()
        def na():
             win.destroy()

        lab= Label(win, text="Do you want", font=("consolas",12,"bold")).pack()
        lab= Label(win, text="to Exit the Table", font=("consolas",12,"bold")).pack()
        but1= Button(win, text="Yes", fg="white",command=adios,bg="sky blue",font=("agency fb",14,"bold"),padx=47)
        but1.pack(side=LEFT)
        but2= Button(win, text="No", fg="white", bg="Red",command=na,font=("agency fb",14,"bold"),padx=50)
        but2.pack(side=LEFT)
        #root.bind('<y>',lambda event:adios())
        #root.bind('<n>',lambda event:na())
        
    bgim= ImageTk.PhotoImage(file="download.jpg")
    back= Label(menu, image=bgim).place(x=0,y=0)
    but1= Button(menu, text="Create",fg="black",command=hello ,bd=5,font=("agency fb" ,25,"bold"), padx=55, pady=3)
    but1.place(x=260, y=160, height=70)
    but1= Button(menu, text="Search Data",command=searching, fg="black",bd=5, font=("agency fb" ,25,"bold"), padx=26, pady=3 )
    but1.place(x=260, y=240, height=70)
    but1= Button(menu, text="Delete",  fg="black",bd=5,command=dele, font=("agency fb" ,25,"bold"), padx=60, pady=3 )
    but1.place(x=260, y=320, height=70)
    but1= Button(menu, text="Show Data", command=show,fg="black",bd=5, font=("agency fb" ,25,"bold"), padx=36, pady=3 )
    but1.place(x=260, y=400, height=70)
    btn2= Button(menu, bd=5,text="Exit", command=exitwin,fg="red" ,font=("agency fb",25,"bold"), padx=14)
    btn2.place(x=590, y=410, height=55)
                   

    menu.mainloop()
