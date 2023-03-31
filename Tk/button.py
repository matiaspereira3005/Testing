from tkinter  import *

root =Tk()
root.title('Hola mundo')
root.geometry('300x300')

l = Label(root, text= "hola mundo")
def click():
    l.pack()

btn = Button(root, text="Clickeame", command=click, fg='white', bg='black')#tambien puede ser hexdgecimal (#fff000)
btn.pack()

root.mainloop()
