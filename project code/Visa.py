from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import qrcode
import string
import random
import sqlite3

def command():
    global _user, _password
    _user = e_1.get()
    _password = password()
    name_file = e_save.get()
    info = qrcode.make(f"user name is ,{_user}, and the password is ,{_password}")
    info.save(r'd:\ ' + name_file + '.jpg')
    messagebox.showinfo(' the file is saved in "D" ')

    db = sqlite3.connect("bank's information.db")
    cr = db.cursor()
    cr.execute("create table if not exists info (name text, password text, money integer, phone text)")
    cr.execute(f"insert into info (name, password, money, phone) values ('{_user.lower().strip()}', '{_password}', 0, '{e_2.get().strip()}')")
    db.commit()
    db.close()

def password():
    all_chars =  string.digits
    count_chars = len(all_chars)    
    serial_list = []
    count = 4
    while count > 0:
        random_number = random.randint(0 , count_chars - 1)
        random_character = all_chars[random_number]
        serial_list.append(random_character)
        count -= 1
    return "".join(serial_list)

window = Tk()
window.geometry('400x600+340+100')
window.resizable(False,False)
window.title("Visa")
icon = PhotoImage(file = r"d:\MSA\python projects\ATM\project code\photos\stamp.png")
window.iconphoto(False, icon)

main_l = Label(window, text=f"Welcome in Visa", font=("Bondi MT", 20), bg='black', fg='white')
main_l.pack(fill=X)

image = PhotoImage(file=r"D:\MSA\Python Projects\ATM\project code\photos\visa.png")
resized_image = image.subsample(1)

label = Label(window, image=resized_image)
label.pack()

l_1 = Label(window, text="user name : ", font=("Bondi MT", 15))
l_1.place(x=10, y=250)

e_1 = Entry(window, font=('Bondi MT', 15), width= 20, fg='white', bg='cornflowerblue')
e_1.place(x= 130, y= 250)

l_2 = Label(window, text=f"your password : {password()} ", font=("Bondi MT", 15))
l_2.place(x= 10, y= 290)

l_3 = Label(window, text="phone :", font=("Bondi MT", 15))
l_3.place(x= 10, y= 330)

e_2 = Entry(window, font=('Bondi MT', 15), width= 20, fg='white', bg='cornflowerblue')
e_2.place(x= 131, y= 330)

l_save = Label(window, text='File Save : ', font=("Bondi MT", 15))
l_save.place(x= 10, y= 382)

e_save = Entry(window, font=('Bondi MT', 15), width= 20, fg='white', bg='cornflowerblue')
e_save.place(x= 131, y= 380)

b_save = Button(window, text='Save ✔', fg='white', bg='red', font=("Bondi MT", 15), command=command, width=31)
b_save.place(x= 20, y= 420)

window.mainloop()

