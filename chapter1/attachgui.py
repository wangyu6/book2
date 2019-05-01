from tkinter import *
from tkinter102 import Mygui

#应用主窗口
mainwin = Tk()
Label(mainwin,text = __name__).pack()


#弹出窗口
popup = Toplevel()
Label(popup,text='attach').pack(side =LEFT)
Mygui(popup).pack(side = RIGHT)
mainwin.mainloop()