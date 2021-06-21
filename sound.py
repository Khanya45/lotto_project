# from playsound import playsound
# # import multiprocessing
# playsound('AUD-20191215-WA0026.mp3')

# import sign_in
import random
import datetime
import rsaidnumber
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Player:

    def __init__(self, name, email, idnumber, address):
        self.name = name
        self.email = email
        self.idnumber = idnumber
        self.address = address


#  ------------ Enter Button on Sign-In -----------------
    def validation(self):
        id = rsaidnumber.parse(self.idnumber)
        #  validating id number
        if id.valid == False:
            messagebox.showerror("", "Invalid ID number")
        #  validating name and address entries
        elif (len(self.name) == 0) or (len(self.address) == 0):
            messagebox.showerror("", "Form incomplete")
        else:
            birth_year = id.date_of_birth.year
            current_date = datetime.date.today()
            current_year = current_date.year
            age = current_year - birth_year
            #  validating age
            if age >= 18:
                messagebox.showinfo("", "LETS PLAY")
                print("YES")
            elif age < 18:
                messagebox.showinfo("", "You are too young to play")
            else:
                messagebox.showerror("", "Invalid ID number")


    def tostring(self, prize, sets):
        return f'{self.playerid_generator()} : {self.name} \n {self.idnumber} \n {sets} \n {prize} \n {self.email} \n {self.address}'


    def playerid_generator(self):
        first_5 = random.randint(10000, 99999)
        second_4 = random.randint(1000, 9999)
        third_3 = random.randint(100, 999)
        last_1 = random.randint(0, 9)
        return (first_5+ second_4+ third_3+ last_1)


    def writeon_file(self):
        with open("playerDetails.txt", "a") as file:
            # text = [name, playerid, sets, prize, contacts]
            file.writelines(self.tostring())


    def send_email(self):
        try:
            sender_email_id = 'khanyagope93@gmail.com'
            receiver_email_id = self.email
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
            messagebox.showinfo("", "Valid email")


objPlayer = Player(sign_in.entyName.get(), sign_in.entyEmail.get(), sign_in.entyID.get())


class Game:
    def __init__(self):
        pass


    def lottogenerator(self, userLotto):
        lotto_prizes = {0: 0, 1: 0, 2: 20, 3: 100.50, 4: 2384, 5: 8584, 6: 10000000}
        count = 0
        # userLotto = []
        winLotto = []
        for i in range(0, 6):
            rand_num = random.randint(1, 49)
            winLotto.append(rand_num)
            # userLotto.append(user_num)
        for i in range(0, 6):
            for y in range(0, 6):
                if userLotto[i] == winLotto[y]:
                    count += 1
        prize = lotto_prizes[count]
        return f'{prize} {userLotto} {winLotto} {count}'



    def playerid_validation(self,playerID):
        if playerID.isdigit() == False or len(playerID) != 13:
            messagebox.showerror("", "Invalid player ID")


#  ---------------- RESET BUTTON -------------------------
    def ResetBtn(self, list):
        with open("sets.txt", "w") as file:
            for i in list:
                file.write(i)


#  --------------- PLAY BUTTON -----------
    def playbtn(self):
        with open("sets.txt", "r") as file:
            for line in file:
                # for number in line:
                sets = line.split()


