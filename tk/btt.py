from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def btt_func():
    print(rd_bool.get())
    rd_bool.set(False)


tk = ttk.Window(themename='journal')
tk.title('test')


# widget
lb = Label(tk, text='Hello, World!', font='arial 24 bold')
lb.pack()

# rd
rd_str = StringVar()
rd_bool = BooleanVar()
rd = Radiobutton(tk, text='radio_button_1', variable=rd_bool, value='True')
rd2 = Radiobutton(tk, text='radiobutton_2', variable=rd_bool, value='False')
rd.pack()
rd2.pack()

# btt
btt = Button(tk, text='push it', command=btt_func)
btt.pack()

tk.mainloop()
