from tkinter import *

root = Tk()
root.configure(background='#333333')
root.title('Calculadora')
root.geometry('348x168')

equation = StringVar()
expression_entry = Entry(root, textvariable=equation)
expression_entry.grid(row=0, columnspan=4, sticky='nswe')

btn7 = Button(root, text= '7', fg='#fff', background= '#666')
btn7.grid(row=1, column=0, sticky='nswe')

btn8 = Button(root, text= '8', fg='#fff', background= '#666')
btn8.grid(row=1, column=1, sticky='nswe')

btn9 = Button(root, text= '9', fg='#fff', background= '#666')
btn9.grid(row=1, column=2, sticky='nswe')

btn4 = Button(root, text= '4', fg='#fff', background= '#666')
btn4.grid(row=2, column=0, sticky='nswe')

btn5 = Button(root, text= '5', fg='#fff', background= '#666')
btn5.grid(row=2, column=1, sticky='nswe')

btn4 = Button(root, text= '4', fg='#fff', background= '#666')
btn4.grid(row=2, column=2, sticky='nswe')

btn1 = Button(root, text= '1', fg='#fff', background= '#666')
btn1.grid(row=3, column=0, sticky='nswe')

btn2 = Button(root, text= '2', fg='#fff', background= '#666')
btn2.grid(row=3, column=1, sticky='nswe')

btn3 = Button(root, text= '3', fg='#fff', background= '#666')
btn3.grid(row=3, column=2, sticky='nswe')

btn0 = Button(root, text= '0', fg='#fff', background= '#666')
btn0.grid(row=4, column=0, sticky='nswe', columnspan=2)

decimal = Button(root, text= ' . ', fg='#fff', background= '#666')
decimal.grid(row=4, column=2, sticky='nswe')

plus = Button(root, text=' + ', fg='#fff', bg='#fe9727')
plus.grid(row=1, column=3, sticky='nswe')

minus = Button(root, text=' - ', fg='#fff', bg='#fe9727')
minus.grid(row=2, column=3, sticky='nswe')

multiply = Button(root, text=' * ', fg='#fff', bg='#fe9727')
multiply.grid(row=3, column=3, sticky='nswe')

divide = Button(root, text=' / ', fg='#fff', bg='#fe9727')
divide.grid(row=4, column=3, sticky='nswe')

equal = Button(root, text=' = ', fg='#fff', bg='#fe9727')
equal.grid(row=5, column=3, sticky='nswe')

clear = Button(root, text='clear', fg='#fff', bg='#999')
clear.grid(row=5, column=2, sticky='nswe')

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()