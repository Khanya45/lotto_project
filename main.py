
import random
import datetime
import rsaidnumber
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#  ------------------------- PLAY UNIT -----------------------------------------
def lottogenerator():
    lotto_prizes = {0: 0, 1: 0, 2: 20, 3: 100.50, 4: 2384, 5: 8584, 6: 10000000}
    count = 0
    userLotto = []
    winLotto = []
    for i in range(0, 6):
        rand_num = random.randint(1, 49)
        winLotto.append(rand_num)
        user_num = int(input("enter the lotto number"))
        userLotto.append(user_num)
    for i in range(0, 6):
        for y in range(0, 6):
            if userLotto[i] == winLotto[y]:
                count += 1
    prize = lotto_prizes[count]
    print(prize)


# lottogenerator()

#  ------------------------------ SIGN IN UNIT ------------------------------------
def age_validation():
    id = rsaidnumber.parse('0210160451089')
    birth_year = id.date_of_birth.year
    current_date = datetime.date.today()
    current_year = current_date.year
    age = current_year - birth_year
    if age >= 18:
        messagebox.showinfo("", "LETS PLAY")
    elif age < 18:
        messagebox.showinfo("", "You are too young to play")
    else:
        messagebox.showerror("", "Invalid ID number")


# age_validation()


def playerid_generator():
    first_5 = random.randint(10000, 99999)
    second_4 = random.randint(1000, 9999)
    third_3 = random.randint(100, 999)
    last_1 = random.randint(0, 9)
    print(first_5 + second_4 + third_3 + last_1)


# playerid_generator()

#  ----------- VALIDATION --------------
def email_validation(email):
    try:
        sender_email_id = 'khanyagope93@gmail.com'
        receiver_email_id = email
        password = "GETRICHWITHLOTTO"
        subject = "Greetings"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = "hi guys how are you. i am doing fine\n"
        body = body + "How was your task yesterday"
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email_id, password)
        s.sendmail(sender_email_id, receiver_email_id, text)
        s.quit()
    except ValueError:
        messagebox.showinfo("", "Valid email")


# email_validation("khanyagope93@gmail.com")


#  ----------------------------------- LOG IN UNIT -------------------------------------

#  ------ PLAYERID VALIDATION ---------
def playerid_validation(playerID):
    if playerID.isdigit() == False or len(playerID) != 13:
        messagebox.showerror("", "Invalid player ID")


#  -------- FINDING PLAYER ACCOUNT
def findplayer(playerid):
    with open("playerDetails.txt", "r") as file:
        for line in file:
            if line.find(playerid):
                pass
            else:
                messagebox.showerror("", "Account not found")



#  ---------------------------------- CLAIM UNIT -----------------------------------

#  ----------- VALIDATION --------------
def validation(accNumber, accHolder, bank):
    if (accNumber.isdigit() == False) or (len(accNumber) < 9):
        messagebox.showerror("", "Invalid Account Number")
    elif (accHolder.isalpha() == False) or (accHolder == ""):
        messagebox.showerror("", "Invalid Account Holder")
    elif bank == "":
        messagebox.showerror("", "Choose the bank")
    else:
        messagebox.showinfo("", "You will hear from us within 10 minutes")



#  ---------- ID NUMBER VALIDATION --------

def id_validation(id):
    try:
        id_number = rsaidnumber.parse(id)
        if id_number.valid:
            messagebox.showerror("", "Valid ID number")
    except:
        messagebox.showerror("", "Invalid ID number")


# id_validation('021016045109')

def email(email):
    with open("sets.txt", "w") as file:
        file.write(f'{email}\n')


email("khanyagope93@gmail.com")
#  ------------------- FILE HANDLING --------------------

#  writing all the player's details and lotto results on a text file
def writeon_file(name, playerid, prize, sets, contacts, id):
    with open("playerDetails.txt", "a") as file:
        text = [name, playerid, sets, prize, contacts]
        file.writelines(text)


# writeon_file("khanya", "8765675432123", "675", "45676545", "khanyagope93@gmail.com", "0210160451089")


def readfile(playerid, idnumber):
    with open("playerDetails.txt", "r") as file:
        for line in file:
            if (playerid in line) or (idnumber in line):
                messagebox.showinfo("", "Lets PLAY!!")
                break
            else:
                messagebox.showerror("", "Your account is not found")


# readfile("87656732123", "0210160451089")

#  ---------------- RESET BUTTON -------------------------
def ResetBtn(list):
    with open("sets.txt", "w") as file:
        for i in list:
            file.write(i)


#  --------------- PLAY BUTTON -----------
def playbtn():
    with open("sets.txt", "r") as file:
        for line in file:
            # for number in line:
            sets = line.split()


def send_email(email):
    try:
        sender_email_id = 'lottowinners957@gmail.com'
        receiver_email_id = email
        password = "GETRICHWITHLOTTO"
        subject = "Greetings"
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
    except ValueError:
        messagebox.showinfo("", "Invalid email")


# send_email('khanyagope93@gmail.com')

def player_numbers():
    list1 = [234, 234, 234, 234, 2343, 4]
    return list1

def store_sets():
        sets = [player_numbers()]
        if len(sets) > 3:
            sets.pop(-1)
            messagebox.showerror("", "Cannot play more than 3 sets")
            # btnReset["state"] = "DISABLED"

#  get prize from textfile
# with open("playerDetails.txt", "r") as file:
#     for line in file:
#         pos1 = line.find("Prize1")
#         pos2 = line.find("Prize2")
#         pos3 = line.find("Prize3")
#     total = line[pos1+1] + line[pos2+1] + line[pos3+1])

# with open("sets.txt", "w") as sfile:
#     sfile.write(f'{player_numbers()}:{prize.get()}\n')
#
#
# with open("sets.txt", "r") as file:
#     count = 0
#     total = 0
#     for line in file:
#         count += 1
#         pos = line.find(":")+1
#         line_lenght = len(line)
#         prize = line[pos:line_lenght]
#         total += prize
#
#     if count == 3:
#         btnReset["state"] = "DISABLED"
#


# def validation(idnumber, address, name):
#         #  validating name and address entries
#         if (len(name) == 0) or (len(address) == 0):
#             messagebox.showerror("", "Form incomplete")
#         else:
#             try:
#                 id_number = rsaidnumber.parse(idnumber)
#                 if id_number.valid:
#                     birth_year = id_number.date_of_birth.year
#                     current_date = datetime.date.today()
#                     current_year = current_date.year
#                     age = current_year - birth_year
#             #  validating age
#                     if age >= 18:
#                         playerid_generator()
#                         writeon_file()
#                         send_email(entyEmail.get())
#                         write_email()
#                 else:
#                     messagebox.showinfo("", "You are too young to play")
#             except:
#                 messagebox.showerror("", "Invalid ID number")


def btnclaim():
        with open("sets.txt") as file:
            line = file.readlines()
            for i in range(len(line)):
                if i == 1:
                    del line[i]
        with open("sets.txt", "w") as new_file:
            for lines in line:
                new_file.write(f'{lines}')


# btnclaim()


def email():
    with open("sets.txt", "r") as pfile:
        line = pfile.readlines()
    print(line[0])


email()
