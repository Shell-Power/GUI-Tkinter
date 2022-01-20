from tkinter import *
from PIL import ImageTk
from management import hello

root= Tk()
root.geometry("800x550")
root.title("LOGIN")
bg= ImageTk.PhotoImage(file="download (1).png")
back= Label(root, image=bg).place(x=0,y=0)
def on_button():
     username=ent1.get()
     password=ent2.get()

     if username=="root":
          pass
     else:
          lab1= Label(root, text="Invalid Username",font=("agency fb", 20,"bold")).place(x=330,y=370)
          print("invalid")

     if password=="management":
          button1= Button(root, text="Login",font=("agency fb", 20), width=10, height=1,command=hello)
          button1.place(x=650, y=450)

     else:
          lab2= Label(root, text="Invalid Password",font=("agency fb", 20,"bold")).place(x=330,y=370)
          print("invalid")

ent1= Entry(root, bd=5, font=("agency fb", 27),width=15)
ent2= Entry(root, bd=5, font=("agency fb", 27),width=15, show="*")
but= Button(root, text="Check Me!",font=("agency fb", 20), width=10, height=1,command=on_button)
ent1.place(x=330,y=166)
ent2.place(x=330,y=285)
but.place(x=650, y=450)

        
root.mainloop()
