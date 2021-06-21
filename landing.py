from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.geometry("550x360")
root.title('SIGNIN')

pic1 = Image.open("landing.jpg")
logo = ImageTk.PhotoImage(pic1)
bg = Label(root, image=logo)
bg.place(x=0, y=0)

def signin():
    root.destroy()
    import sign_in

def login():
    root.destroy()
    import log_in


btnSign = Button(root, text="SIGN IN", height=5, width=10, font="Times 20", command=signin)
btnSign.place(x=100, y=100)

btnLog = Button(root, text="LOG IN", height=5, width=10, font="Times 20", command=login)
btnLog.place(x=300, y=100)

root.mainloop()
