# with open("sets.txt") as file:
#     line = file.readlines()
# del line[1]
#
# with open("sets.txt", "w") as new_file:
#     for lines in line:
#         new_file.write(f'{lines}')
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")
#
entyPlayer = Entry(root)
entyPlayer.pack()



#  function for extracting an email from a textfile for log in players
# def email(id):
#     with open("playerDetails.txt", "r") as file:
#         lines = file.readlines()
#         pos = 0
#         for line in file:
#             # global pos
#             pos = line.find(id)+1
#         if pos > 1:
#             email = lines[pos]
#             print(email)
#         else:
#             print("ID number not found")
person_id = ""


def emailing(id):
    with open("playerDetails.txt", "r") as file:
        for line in file:
            if id in line:
                global person_id
                person_id = line
        if not len(person_id) > 1:
            print("Id not found.")
        print(person_id)



btn = Button(root, command=emailing(entyPlayer.get()))
btn.pack()


root.mainloop()
# with open("sets.txt", "r") as file:
#     total = 0
#     for line in file:
#         if "khnyagope93@gmail.com" not in line:
#             pos = line.find(":")+1
#             line_lenght = len(line)
#             prize = float(line[pos:line_lenght])
#             total += prize
#     print(total)

