from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import Mygui

class Customgui(Mygui):
    def reply(self):
        showinfo(title='popup',message='啊啊')

if __name__ =='__main__':
    Customgui().pack()
    mainloop()
