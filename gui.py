from tkinter import *

def instant():
   root = Tk()
   root.geometry("750x100")
   root['background']="black"
   def a():
      lol=Label(root,bg="black",fg="#00ff00", text=".- ", font=('system 20 bold')).pack(side=LEFT)
   def b():
      lol=Label(root,bg="black",fg="#00ff00", text="-... ", font=('system 20 bold')).pack(side=LEFT)
   def c():
      lol=Label(root,bg="black",fg="#00ff00", text="-.-. ", font=('system 20 bold')).pack(side=LEFT)
   def d():
      lol=Label(root,bg="black",fg="#00ff00", text="-.. ", font=('system 20 bold')).pack(side=LEFT)
   def e():
      lol=Label(root,bg="black",fg="#00ff00", text=". ", font=('system 20 bold')).pack(side=LEFT)
   def f():
      lol=Label(root,bg="black",fg="#00ff00", text="..-. ", font=('system 20 bold')).pack(side=LEFT)
   def g():
      lol=Label(root,bg="black",fg="#00ff00", text="--. ", font=('system 20 bold')).pack(side=LEFT)
   def h():
      lol=Label(root,bg="black",fg="#00ff00", text=".... ", font=('system 20 bold')).pack(side=LEFT)
   def i():
      lol=Label(root,bg="black",fg="#00ff00", text=".. ", font=('system 20 bold')).pack(side=LEFT)
   def j():
      lol=Label(root,bg="black",fg="#00ff00", text=".--- ", font=('system 20 bold')).pack(side=LEFT)
   def k():
      lol=Label(root,bg="black",fg="#00ff00", text="-.- ", font=('system 20 bold')).pack(side=LEFT)
   def l():
      lol=Label(root,bg="black",fg="#00ff00", text=".-.. ", font=('system 20 bold')).pack(side=LEFT)
   def m():
      lol=Label(root,bg="black",fg="#00ff00", text="-- ", font=('system 20 bold')).pack(side=LEFT)
   def n():
      lol=Label(root,bg="black",fg="#00ff00", text="-. ", font=('system 20 bold')).pack(side=LEFT)
   def o():
      lol=Label(root,bg="black",fg="#00ff00", text="--- ", font=('system 20 bold')).pack(side=LEFT)
   def p():
      lol=Label(root,bg="black",fg="#00ff00", text=".--. ", font=('system 20 bold')).pack(side=LEFT)
   def r():
      lol=Label(root,bg="black",fg="#00ff00", text="-.- ", font=('system 20 bold')).pack(side=LEFT)
   def s():
      lol=Label(root,bg="black",fg="#00ff00", text="... ", font=('system 20 bold')).pack(side=LEFT)
   def t():
      lol=Label(root,bg="black",fg="#00ff00", text="- ", font=('system 20 bold')).pack(side=LEFT)
   def u():
      lol=Label(root,bg="black",fg="#00ff00", text="..- ", font=('system 20 bold')).pack(side=LEFT)
   def v():
      lol=Label(root,bg="black",fg="#00ff00", text="...- ", font=('system 20 bold')).pack(side=LEFT)
   def w():
      lol=Label(root,bg="black",fg="#00ff00", text=".-- ", font=('system 20 bold')).pack(side=LEFT)
   def x():
      lol=Label(root,bg="black",fg="#00ff00", text="-..- ", font=('system 20 bold')).pack(side=LEFT)
   def y():
      lol=Label(root,bg="black",fg="#00ff00", text="-.-- ", font=('system 20 bold')).pack(side=LEFT)
   def z():
      lol=Label(root,bg="black",fg="#00ff00", text="--.. ", font=('system 20 bold')).pack(side=LEFT)
   def space():
      lol=Label(root,bg="black",fg="#00ff00", text="/ ", font=('system 20 bold')).pack(side=LEFT)
      


   root.bind('<a>',lambda event:a())
   root.bind('<b>',lambda event:b())
   root.bind('<c>',lambda event:c())
   root.bind('<d>',lambda event:d())
   root.bind('<e>',lambda event:e())
   root.bind('<f>',lambda event:f())
   root.bind('<g>',lambda event:g())
   root.bind('<h>',lambda event:h())
   root.bind('<i>',lambda event:i())
   root.bind('<j>',lambda event:j())
   root.bind('<k>',lambda event:k())
   root.bind('<l>',lambda event:l())
   root.bind('<m>',lambda event:m())
   root.bind('<n>',lambda event:n())
   root.bind('<o>',lambda event:o())
   root.bind('<p>',lambda event:p())
   root.bind('<q>',lambda event:q())
   root.bind('<r>',lambda event:r())
   root.bind('<s>',lambda event:s())
   root.bind('<t>',lambda event:t())
   root.bind('<u>',lambda event:u())
   root.bind('<v>',lambda event:v())
   root.bind('<w>',lambda event:w())
   root.bind('<x>',lambda event:x())
   root.bind('<y>',lambda event:y())
   root.bind('<z>',lambda event:z())
   root.bind('<space>',lambda event:space())

   root.mainloop()
