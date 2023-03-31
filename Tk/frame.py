from tkinter import *

root =Tk()
root.title('Hola mundo')

#frame = LabelFrame(root, text='Login',padx=10, pady=10, borderwidth=10)
#frame = LabelFrame(root,padx=10, pady=10, borderwidth=10)
frame = Frame(root,padx=10, pady=10, borderwidth=10)
frame.pack(padx=50, pady=50)

frame.pack()
l = Label(frame, text='Estoy dentro del frame')
btn = Button(frame, text="salir", command=root.quit)
l.pack()
btn.pack()

root.mainloop()
