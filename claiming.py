from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests


root = Tk()
root.geometry("460x500")
root.title('CLAIM PRIZE')
root.config(bg='#f48c06')


def exit():
    root.destroy()

#  FUNCTIION FOR SENDING AN EMAIL TO THE PLAYER
def send_email(email):
    try:
        #  IF EVER THE EMAIL IS VALID , THE FOLLIOWING CODE WILL BE EXECUTED
        sender_email_id = 'lottowinners957@gmail.com'
        receiver_email_id = email
        password = "GETRICHWITHLOTTO"
        subject = "Your Details"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = f'bank account details: \n Bank: {cbBank.get()} \n Account Holder: {entyAccHolder.get()} \n Account Number: {entyAccNumber.get()}'
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, password)
        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()
    except ValueError:
        # ELSE IF THERE ARE ANY ERRORS(INVALID EMAIL OR NO CONNECTION, THE FOLLOWING CODE WILL BE EXECUTED)
        messagebox.showinfo("", "No internet connection")
    #  the messagebox will display when the email is sent
    messagebox.showinfo("", "Check your email for further instructions")


#  this fuction is for validating the account holder and account number
def validation(accHolder, accNum):
    if (len(accHolder) == 0) or (len(accNum == 0)) or (accNum < 9):
        messagebox.showerror("", "Invalid info. Please try again")


#  FUNCTION FOR EXTRACTING AN EMAIL FROM A TEXTFILE for sign in players
def email():
    with open("sets.txt", "r") as pfile:
        line = pfile.readlines()
    return line[0]


#  FUNCTION FOR DELETING THE LAST 3 LINES FROM THE TEXTFILE
def delete_lines():
        with open("sets.txt") as file:
            line = file.readlines()
            for i in range(len(line)):
                if i == 1:
                    del line[i]
        with open("sets.txt", "w") as new_file:
            for lines in line:
                new_file.write(f'{lines}')


#  CALCULATING THE TOTAL PRIZE OF THE PLAYER BY EXTRACTING AND ADDING EACH WIN PRIZE FROM A TEXTFILE
with open("sets.txt", "r") as file:
    total = 0
    email = email()
    for line in file:
        if email not in line:
            pos = line.find(":")+1
            line_lenght = len(line)
            prize = float(line[pos:line_lenght])
            total += prize


#  COMBOBOX FOR CURRENCIES
lbCurrency = Label(root, text="Choose currency(USD)", bg='#f48c06')
lbCurrency.place(x=80, y=290)
cbCurrency = ttk.Combobox(root)
cbCurrency.place(x=80, y=310, width=70)
response = requests.get('https://v6.exchangerate-api.com/v6/fac9f0aa288dff6d0a7c7a88/latest/USD')
text = response.json()
conversion_rates = text['conversion_rates'].keys()
rates = list(conversion_rates)
cbCurrency['values'] = rates


def converter():
    convert = total * text['conversion_rates'][cbCurrency.get()]
    print(convert)


pic1 = Image.open("logo.png")
resize = pic1.resize((100, 80), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=350, y=5)


#  HEADING
lbHeading = Label(root, text='Banking Details', font='Times 30', bg='#f48c06')
lbHeading.place(x=80, y=40)


#  ENTRIES
lbAccHolder = Label(root, text='Account Holder Name', bg='#f48c06')
lbAccHolder.place(x=80, y=120)
entyAccHolder = Entry(root, width=30)
entyAccHolder.place(x=80, y=145)

lbAccNumber = Label(root, text='Account Number', bg='#f48c06')
lbAccNumber.place(x=80, y=180)
entyAccNumber = Entry(root, width=30)
entyAccNumber.place(x=80, y=200)

#  COMBOBOX FOR BANK TYPE
lbBank = Label(root, text='Bank', bg='#f48c06')
lbBank.place(x=80, y=235)
cbBank = ttk.Combobox(root)
cbBank['values'] = ["ABSA", "CAPITEC", "FNB", "STANDARD BANK"]
cbBank.place(x=80, y=255)


#  BUTTTONS

#  the button will firstly execute the send_email function and then the validation function
# btnSubmit = Button(root, text='SUBMIT', width=20, borderwidth=3, command=lambda: [converter(), send_email(email()), validation(entyAccHolder.get(), entyAccNumber.get()), delete_lines()])
btnSubmit = Button(root, text='SUBMIT', width=20, borderwidth=3, command=lambda: [send_email(email())])
btnSubmit.place(x=80, y=370)
btnExit = Button(root, text='EXIT', borderwidth=7, command=exit)
btnExit.place(x=80, y=420)


root.mainloop()
