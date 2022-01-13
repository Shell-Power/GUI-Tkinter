from tkinter import *
root= Tk()
root.geometry("400x400")
root['background']='black'

def buttoncom():
     text=E1.get()
     print(text)
     return None

l1 = Label(root,text="TEXT Over Here :",bg="black",fg="#00FF00",padx=50, pady=20, font=("consolas", 20))
l1.pack()
E1 = Entry(bd =7, font=("consolas",15),fg="cyan", bg="#32CD32")
E1.pack(ipadx=20, ipady=10)
button=Button(root, text="Generate",padx=50, pady=20,fg="#00FF00",bg="grey",
                       font=("consolas",15), command= buttoncom).pack(padx=50,pady=100)


root.mainloop()








