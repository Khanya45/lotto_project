from tkinter import *
from tkinter import messagebox
import random
from PIL import ImageTk, Image
from playsound import playsound
import multiprocessing
from tkinter import ttk
import requests

root = Tk()
root.geometry("459x520")
root.title('PLAY')
root.config(bg='#f48c06')


class clsPlay:

    def __init__(self, root):
        self.lbUser_lotto_num = Label(root, text='User Lottery Number:', bg='#f48c06')
        self.lbUser_lotto_num.place(x=50, y=40)
        # six entries to enter lottery numbers
        self.entyUser_1 = Spinbox(root, width=3, from_=1, to=49)
        self.entyUser_1.place(x=50, y=70)
        self.entyUser_2 = Spinbox(root, width=3, from_=1, to=49)
        self.entyUser_2.place(x=100, y=70)
        self.entyUser_3 = Spinbox(root, width=3, from_=1, to=49)
        self.entyUser_3.place(x=150, y=70)
        self.entyUser_4 = Spinbox(root, width=3, from_=1, to=49)
        self.entyUser_4.place(x=200, y=70)
        self.entyUser_5 = Spinbox(root, width=3, from_=1, to=49)
        self.entyUser_5.place(x=250, y=70)
        self.entyUser_6 = Spinbox(root, width=3, from_=1, to=49)
        self.entyUser_6.place(x=300, y=70)
        self.lbUser_lotto_num = Label(root, text='Winning Lottery Number:', bg='#f48c06')
        self.lbUser_lotto_num.place(x=50, y=150)
        # six entries for winning lottery numbers
        self.entyWin_1 = Entry(root, width=5)
        self.entyWin_1.place(x=50, y=180)
        self.entyWin_2 = Entry(root, width=5)
        self.entyWin_2.place(x=100, y=180)
        self.entyWin_3 = Entry(root, width=5)
        self.entyWin_3.place(x=150, y=180)
        self.entyWin_4 = Entry(root, width=5)
        self.entyWin_4.place(x=200, y=180)
        self.entyWin_5 = Entry(root, width=5)
        self.entyWin_5.place(x=250, y=180)
        self.entyWin_6 = Entry(root, width=5)
        self.entyWin_6.place(x=300, y=180)
        self.lbUser_lotto_num = Label(root, text='Number of matches:', bg='#f48c06')
        self.lbUser_lotto_num.place(x=50, y=260)
        self.entyMatches = Entry(root, width=7)
        self.entyMatches.place(x=50, y=290)
        self.lbUser_lotto_num = Label(root, text='Prize:', bg='#f48c06')
        self.lbUser_lotto_num.place(x=220, y=260)



         #  An entry for number of matches
        self.entyPrize = Entry(root, width=10)
        self.entyPrize.place(x=220, y=290)
         #  button for lottery generator  , self.sound(self.entyPrize.get())
        self.btnPlay = Button(root, text='PLAY', width=10, borderwidth=3, command=lambda: [self.lottogenerator(self.player_numbers()), self.savegame()])
        self.btnPlay.place(x=50, y=390)
        #  button for playing again/clearing the entries
        self.btnReset = Button(root, text='RESET', width=10, borderwidth=3, command=self.ResetBtn)
        self.btnReset.place(x=175, y=390)
        # This button is going to display when the entry of the prize is greater than 0
        self.btnClaim = Button(root, text='CLAIM', width=10, borderwidth=3, command=self.next_window)
        self.btnClaim.place(x=300, y=390)
        #  button for exiting
        self.btnExit = Button(root, text='EXIT', font='bold', borderwidth=7, command=exit)
        self.btnExit.place(x=170, y=470)
        self.pic1 = Image.open("logo.png")
        self.resize = pic1.resize((100, 60), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(resize)
        self.lbpic = Label(root, image=logo, bg='#f48c06')
        self.lbpic.place(x=350, y=5)


    def player_numbers(self):
        userLotto = []
        userLotto.extend([self.entyUser_1.get(), self.entyUser_2.get(), self.entyUser_3.get(), self.entyUser_4.get(), self.entyUser_5.get(), self.entyUser_6.get()])
        return userLotto


#  ---------------- RESET BUTTON -------------------------
    def ResetBtn(self):
        count = 0
        with open("sets.txt", "r") as file:
            for lines in file:
                count += 1
        if count == 4:
            self.btnReset["state"] = "disabled"
            messagebox.showerror("", "Cannot play more than 3 sets")
        else:
            with open("sets.txt", "a") as sfile:
                sfile.write(f'{self.player_numbers()}:{self.entyPrize.get()}\n')
                self.entyPrize.delete(0, END)
                self.entyMatches.delete(0, END)
                self.entyUser_6.delete(0, END)
                self.entyWin_6.delete(0, END)
                self.entyWin_5.delete(0, END)
                self.entyWin_3.delete(0, END)
                self.entyWin_4.delete(0, END)
                self.entyWin_2.delete(0, END)
                self.entyWin_1.delete(0, END)
                self.entyUser_5.delete(0, END)
                self.entyUser_4.delete(0, END)
                self.entyUser_3.delete(0, END)
                self.entyUser_2.delete(0, END)
                self.entyUser_1.delete(0, END)


    def exit(self):
        root.destroy()


    #  FUNCTION FOR GENERATING RANDOM NUMBERS WITHOUT DUPLICATION AND
    #  STORING THEM IN A LIST AND DISPLAYING THE LIST ON ENTRIES
    def lottogenerator(self, userLotto):
        lotto_prizes = {0: 0, 1: 0, 2: 20, 3: 100.50, 4: 2384, 5: 8584, 6: 10000000}
        count = 0
        winLotto = random.sample(range(1, 49), 6)
        #  comparing the list for random numbers and user lotto numbers
        for i in range(0, 6):
            for y in range(0, 6):
                #  when numbers are equal from both lists , count will be incremented
                if int(userLotto[i]) == winLotto[y]:
                    count += 1
        self.entyMatches.insert(0, count)
        self.entyWin_1.insert(0, winLotto[0])
        self.entyWin_2.insert(0, winLotto[1])
        self.entyWin_3.insert(0, winLotto[2])
        self.entyWin_4.insert(0, winLotto[3])
        self.entyWin_5.insert(0, winLotto[4])
        self.entyWin_6.insert(0, winLotto[5])
        prize = lotto_prizes[count]
        self.entyPrize.insert(0, prize)
        if int(self.entyPrize.get()) > 0:
            playsound('Here comes the money [SOUND EFFECT].mp3')
        else:
            playsound('Fail Sound Effect(1).mp3')


    def savegame(self):
        count = 0
        with open("sets.txt", "r") as file:
            for lines in file:
                count += 1
        if count == 4:
            self.btnPlay["state"] = "disabled"
            messagebox.showerror("", "Cannot play more than 3 sets")
        else:
            with open("playerDetails.txt", "a") as file:
                file.write(f'sets: {self.player_numbers()} \n Matches: {self.entyMatches.get()} \n Prize: {self.entyPrize.get()}\n')


    def next_window(self):
        root.destroy()
        import claiming


pic1 = Image.open("logo.png")
resize = pic1.resize((100, 60), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resize)
lbpic = Label(root, image=logo, bg='#f48c06')
lbpic.place(x=350, y=5)


objPlay = clsPlay(root)
root.mainloop()
