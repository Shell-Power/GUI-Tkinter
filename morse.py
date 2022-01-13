from tkinter import *
from gui import instant
root= Tk()
root.geometry("500x500")
root.title('Morse Code Generator')
root['background']='black'
#root.wm_attributes('-transparentcolor','black')


code={'A' or 'a':'.-  ', 'B' or 'b':'-...  ',' ': '/',
          'C' or 'c':'-.-.  ', 'D' or 'd':'-..  ', 'E' or 'e':'.  ',
          'F' or 'f':'..-.  ', 'G' or 'g':'--.  ', 'H' or 'h':'....  ',
          'I' or 'i':'..  ', 'J' or 'j':'.---  ', 'K' or 'k':'-.-  ',
                     'L' or 'l':'.-..  ', 'M' or 'm':'--  ', 'N' or 'n':'-.  ',
                     'O' or 'o':'---  ', 'P' or 'p':'.--.  ', 'Q' or 'q':'--.-  ',
                     'R' or 'r':'.-.  ', 'S' or 's':'...  ', 'T' or 't':'-  ',
                     'U' or 'u':'..-  ', 'V' or 'v':'...-  ', 'W' or 'w':'.--  ',
                     'X' or 'x':'-..-  ', 'Y' or 'y':'-.--  ', 'Z' or 'z':'--..  ',
                     '1':'.----', '2':'..---', '3':'...--',
                     '4':'....-', '5':'.....', '6':'-....',
                     '7':'--...', '8':'---..', '9':'----.',
                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
                     '?':'..--..', '':'-..-.', '-':'-....-',
                     '(':'-.--.', ')':'-.--.-'}


def buttoncom():
     text=E1.get()
     for i in text:
          final=code[i]
          labelX= Label(root, text=final, bg="black",fg="#00ff00", font=("consolas",20), pady=10)
          labelX.pack(side=LEFT)
     print(labelX)

def close():
     root.destroy()

 
l1 = Label(root,text="TEXT Over Here :",bg="black",fg="#00FF00",padx=50, pady=20, font=("consolas", 20))
l1.pack()
E1 = Entry(bd =7, font=("consolas",15),fg="cyan", bg="green")
E1.pack(ipadx=20, ipady=10)
button=Button(root, text="Generate",padx=20, pady=10,fg="#00FF00",bg="grey",
                       font=("consolas",15), command= buttoncom).pack(pady=15)
button1=Button(root, text="EXIT",padx=42, pady=10,fg="#00FF00",bg="grey",
                       font=("consolas",15), command=close ).pack()
button2= Button(root, text="Instant Mode", pady=10,fg="#00ff00", bg="grey", font=("consolas",15),
                command=instant).pack(pady=15)
root.mainloop()








