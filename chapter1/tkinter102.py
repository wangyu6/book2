from tkinter import *
from tkinter.messagebox import showinfo


# def reply():
#     showinfo(title='pop up',message="button pressed")
# window = Tk()
# button = Button(window,text = 'press',command = reply)
# button.pack()

class Mygui(Frame):
    def __init__(self,parent = None):
        Frame.__init__(self,parent)
        button = Button(self,text='press',command=self.reply)
        button.pack()
    
    def reply(self):
        showinfo(title='pop up',message='button pressed')

if __name__=='__main__':
    window = Mygui()
    window.pack()

    window.mainloop()