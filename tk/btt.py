from tkinter import *

tk = Tk()
tk.title('test')


# widget
lb = Label(tk, text='Hello, World!', font='arial 24 bold')
lb.pack()
rd = Radiobutton(tk, text='radiobtt')
rd.pack()
btt = Button(tk, text='push it')
btt.pack()

tk.mainloop()
