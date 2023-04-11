from tkinter import *
# import ttkbootstrap as ttk


def convert():
    inputs = entry_int.get()
    dolar = (inputs + 0.92)
    output_str.set(f'${dolar}')


# main
tk = Tk()
tk.title('Olá')
tk.geometry("400x150")

# title
label = Label(master=tk, text='Euro to dolar conversion', font='Arial 24 bold')
label.pack()

# input
frame = Frame(master=tk)
entry_int = DoubleVar()
entry = Entry(master=frame, textvariable=entry_int)
button = Button(master=frame, text='press', command=convert)
entry.pack(side='left')
button.pack(side='left')
frame.pack()
# output
output_str = StringVar()
output = Label(master=tk, text='output', textvariable=output_str)
output.pack()

# run
tk.mainloop()
