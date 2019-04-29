from tkinter import *
from tkinter.messagebox import showinfo
def reply():
    showinfo(title='pop up',message="button pressed")
window = Tk()
button = Button(window,text = 'pass',command = reply)
button.pack()



window.mainloop()