from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import rsaidnumber

def exit():
    root.destroy()


#  function for validating the player
# def playerid_validation(playerID):
#     if playerID.isdigit() == False or len(playerID) != 13:
#         messagebox.showerror("", "Invalid player ID")

def check_id():
    id_validation(entyID.get())
    with open("playerDetails.txt", "r") as file:
        for line in file:
            if entyID.get() in line:
                global person_id
                person_id = line
        if len(person_id) < 1:
            messagebox.showerror("", "Id not found.")
        new_window()


def id_validation(id):
    id_number = ""
    try:
        id_number = rsaidnumber.parse(id)
    except:
        messagebox.showerror("", "Invalid ID number")
    if id_number.valid:
            messagebox.showerror("", "valid ID number")


root = Tk()
root.geometry("650x450")
root.title('LOGIN')
root.config(bg='#f48c06')


#  DISPLAYING IMAGES
#  logo image
pic1 = Image.open("logo.png")
resize = pic1.resize((100, 60), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=540, y=5)

#  welcome image
pic = Image.open("welcome.png")
resized = pic.resize((260, 350), Image.ANTIALIAS)


#  HEADING
lbTitle = Label(root, text='LOG IN', font='Times 30', bg='#f48c06')
lbTitle.place(x=380, y=40)

img = ImageTk.PhotoImage(resized)
lbpic = Label(root, image=img, bg='#f48c06')
lbpic.place(x=40, y=50)


#  LABELS AND ENTRIES
lbID = Label(root, text='ID Number', bg='#f48c06')
lbID.place(x=330, y=150)
entyID = Entry(root, width=30)
entyID.place(x=330, y=180)


#  FUNCTION TO IMPORT THE NEXT WINDOW
def new_window():
    root.destroy()
    import play

#  BUTTONS
btnEnter = Button(root, text='ENTER', width=20, borderwidth=3, command=check_id)
btnEnter.place(x=330, y=235)

btnExit = Button(root, text='EXIT', borderwidth=7, command=exit)
btnExit.place(x=330, y=300)

root.mainloop()
