from tkinter import *

root = Tk()
root.title('hola mundo')
root.geometry('500x500')

l1 = Label(root, text='hola mundo! primera etiqueta')
l2 = Label(root, text='chao mundo! segunda etiqueta')

l1.grid(row=0, column=0)
l2.grid(row=1, column=1)

root.mainloop()
