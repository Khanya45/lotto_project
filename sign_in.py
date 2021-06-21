from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import rsaidnumber
import datetime

root = Tk()
root.geometry("660x500")
root.title('SIGNIN')
root.config(bg='#f48c06')


def id_validation(id):
    try:
        id_number = rsaidnumber.parse(id)
        if id_number.valid:
            messagebox.showerror("", "Valid ID number")
    except:
        messagebox.showerror("", "Invalid ID number")


#

def validation(idnumber, address, name):
        #  validating name and address entries
        if (len(name) == 0) or (len(address) == 0):
            messagebox.showerror("", "Form incomplete")
        else:
            id_number = rsaidnumber.parse(idnumber)
            birth_year = id_number.date_of_birth.year
            current_date = datetime.date.today()
            current_year = current_date.year
            age = current_year - birth_year
            #  validating age
            if age >= 18:
                writeon_file()
                send_email(entyEmail.get())
                write_email()
            elif age < 18:
                messagebox.showinfo("", "You are too young to play")
            else:
                messagebox.showerror("", "Invalid ID number")



def playerid_generator():
        first_5 = random.randint(10000, 99999)
        second_4 = random.randint(1000, 9999)
        third_3 = random.randint(100, 999)
        last_1 = random.randint(0, 9)
        return (str(first_5)+ str(second_4)+ str(third_3)+ str(last_1))


def tostring():
    current_date = datetime.date.today()
    # current_time = datetime.time.
    return f'{playerid_generator()} : {entyName.get()} \n {current_date} \n {entyID.get()}\n {entyEmail.get()} \n {entyAddress.get()}'


def writeon_file():
        with open("playerDetails.txt", "a") as file:
            file.write(f'{tostring()}\n')


def send_email(email):
    try:
        import pdb;pdb.set_trace()
        sender_email_id = 'lottowinners957@gmail.com'
        receiver_email_id = email
        password = "GETRICHWITHLOTTO"
        subject = "Account Verification"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = "Your account is verified\n"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, password)
        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()
    except:
        messagebox.showinfo("", "Invalid email")


def play():
    root.destroy()
    import play

pic1 = Image.open("logo.png")
resize = pic1.resize((100, 80), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=550, y=5)

lbTitle = Label(root, text='SIGN IN', font='Times 30', bg='#f48c06')
lbTitle.place(x=380, y=40)

pic = Image.open("lotto.jpeg")
resized = pic.resize((260, 410), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized)
lbpic = Label(root, image=img, bg='#f48c06')
lbpic.place(x=40, y=50)

lbName = Label(root, text='Name', bg='#f48c06')
lbName.place(x=330, y=120)
entyName = Entry(root, width=30)
entyName.place(x=330, y=145)


lbEmail = Label(root, text='Email', bg='#f48c06')
lbEmail.place(x=330, y=180)
entyEmail = Entry(root, width=30)
entyEmail.place(x=330, y=200)



def write_email():
    with open("sets.txt", "w") as file:
        file.write(f'{entyEmail.get()}\n')
    play()



lbAddress = Label(root, text='Address', bg='#f48c06')
lbAddress.place(x=330, y=235)
entyAddress = Entry(root, width=30)
entyAddress.place(x=330, y=255)


lbID = Label(root, text='ID number', bg='#f48c06')
lbID.place(x=330, y=290)
entyID = Entry(root, width=30)
entyID.place(x=330, y=310)


btnEnter = Button(root, text='ENTER', width=20, borderwidth=3, command=lambda: [id_validation(entyEmail.get()), validation(entyID.get(), entyAddress.get(), entyName.get()), writeon_file(), write_email()])
btnEnter.place(x=355, y=370)


btnExit = Button(root, text='EXIT', borderwidth=5, command=exit)
btnExit.place(x=330, y=430)


root.mainloop()
