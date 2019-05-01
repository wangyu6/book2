from tkinter import *
from tkinter.messagebox import showinfo
def reply(name):
    showinfo(title= 'reply',message = 'hello %s ! ' %name)

top  = Tk()
top.title('echo')
top.iconbitmap('1.ico')


Label(top,text = 'enter your name,').pack(side = TOP)
ent = Entry(top)
ent.pack(side = TOP)
btn = Button(top,text = "subbmit",command = (lambda:reply(ent.get())))
btn.pack(side=LEFT)
top.mainloop()

