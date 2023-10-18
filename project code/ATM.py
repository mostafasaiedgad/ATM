import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.messagebox import askyesno
from pywhatkit import sendwhatmsg
import datetime
import os
import cv2
import sqlite3
import string
import random

db = sqlite3.connect("bank's information.db")
cr = db.cursor()

class Main_Window:
    
    def __init__(self):
        self.window = Tk()
        self.window.geometry('600x770+340+100')
        self.window.title('ATM')
        icon = PhotoImage(file=r"d:\MSA\python projects\ATM\project code\photos\atm1.png")
        self.window.iconphoto(False, icon)
        self.window.resizable(False, False)
        self.window.configure(bg="#228B22")
        self.window.protocol("WM_DELETE_WINDOW", self.save)

        self.text_1 = Label(self.window, text='Welcome to ATM', fg='black', bg='#696969', font=("Bondi MT", 20))
        self.text_1.pack(fill=X)

        self.text_2 = Label(self.window, text='Please, Enter your Visa :', fg="black", bg="#228B22", font=("Bondi MT", 15))
        self.text_2.place(x=15, y=180)

        self.e_1 = Entry(self.window, font=("Bondi MT", 15), width=13, bg='#696969', fg='white')
        self.e_1.place(x=345, y=182)   

        self.b_1 = Button(self.window, text='Select Visa', fg='black', bg='#FFC125', width=31, font=("Bondi MT", 15), command=self.open)
        self.b_1.place(x=20, y=240)

        self.b_2 = Button(self.window, text='Read Visa', fg='black', bg='#FFC125', width=31, font=("Bondi MT", 15), command=self.commands)
        self.b_2.place(x=20, y=310)  

    def clear_text(self):
        self.e_1.delete(0, END)

    def open(self):
        self.clear_text()
        file = filedialog.askopenfile(mode='r', filetypes=[('files', '*.jpg'), ('files', '*.png')])
        if file:
            filepath = os.path.abspath(file.name)
            self.e_1.insert(0, str(filepath))   

    def read(self):
        global user_name, password
        d = self.e_1.get()
        if os.path.isfile(d):
            res = cv2.QRCodeDetector()
            val, points, s_qr = res.detectAndDecode(cv2.imread(d))
            if val:
                t = str(val).split(',')
                user_name = t[1]
                password = t[-1]
            else:
                print("QR code not found")
        else:
            print("Invalid file path")

    def check(self):
        global user_name, password
        info = []
        cr.execute(f"select * from info where name = '{user_name}'")
        info = cr.fetchall()
        if info == []:
            messagebox.showinfo('Error', 'You are not found')
        else:
            users = []
            for rows in info:
                users.append(str(rows[0]))
            if str(user_name) in users:
                options = Options(self, user_name, password)
            else:
                messagebox.showinfo("you are not found")
    
    def save(self):
        if askyesno(title='Exit', message='Do you want to exit ?'):
            db.commit()
            db.close()
            self.window.destroy()

    def commands(self):
        self.read()
        self.check()
        self.clear_text()

main_window = Main_Window()

class Options:
    
    def __init__(self, main_window, user_name, password):
        self.window = Toplevel(main_window.window)
        self.window.geometry('600x770+340+100')
        self.window.title('ATM')
        icon = PhotoImage(file=r"d:\MSA\python projects\ATM\project code\photos\atm1.png")
        self.window.iconphoto(False, icon)
        self.window.resizable(False, False)
        self.window.configure(bg="#228B22")

        self.user_name = user_name

        self.text_1 = Label(self.window, text=f'Hello, {user_name}.\nPlease choose an option', fg='black', bg='#696969', font=("Bondi MT", 20))
        self.text_1.pack(fill=X)

        self.b_1 = Button(self.window, text= 'Deposit', fg= 'white', bg= '#FFC125', width= 31, font=("Bondi MT", 15),
                        command=lambda: Password(self, self.user_name, password, button='Deposit'))
        self.b_1.place(x= 20, y= 150)

        self.b_2 = Button(self.window, text= 'Balance', fg= 'white', bg= '#FFC125', width= 31, font=("Bondi MT", 15),
                        command=lambda: Password(self, self.user_name, password, button='Balance'))
        self.b_2.place(x= 20, y= 220)

        self.b_3 = Button(self.window, text= 'Withdraw', fg= 'white', bg= '#FFC125', width= 31, font=("Bondi MT", 15),
                        command=lambda: Password(self, self.user_name, password, button='Withdraw'))
        self.b_3.place(x= 20, y= 290)

        self.b_3 = Button(self.window, text= 'Change Password', fg= 'white', bg= '#FFC125', width= 31, font=("Bondi MT", 15),
                        command=lambda: Change_Password(self, self.user_name, password, button='Change Password'))
        self.b_3.place(x= 20, y= 360)

        self.b_3 = Button(self.window, text= 'Quit', fg= 'white', bg= '#FFC125', width= 31, font=("Bondi MT", 15),
                        command=self.window.destroy)
        self.b_3.place(x= 20, y= 430)

class Password:
    
    def __init__(self, main_window, user_name, password, button):
        self.window = Toplevel(main_window.window)
        self.window.geometry('600x770+340+100')
        self.window.title('ATM')
        icon = PhotoImage(file=r"d:\MSA\python projects\ATM\project code\photos\atm1.png")
        self.window.iconphoto(False, icon)
        self.window.resizable(False, False)
        self.window.configure(bg="#228B22")

        self.password = password
        self.button = button
        self.user_name = user_name

        self.text_1 = Label(self.window, text='Enter your password, please', fg='black', bg='#696969', font=("Bondi MT", 20))
        self.text_1.pack(fill=X)

        self.e_1 = Entry(self.window, font=("Bondi MT", 15), width=33, bg='#696969', fg='white', show='*')
        self.e_1.place(x=20, y=150)

        self.b_1 = Button(self.window, text='Check', fg='white', bg='#FFC125', width=31, font=("Bondi MT", 15),
                        command=lambda: self.check_password(self.password, self.button, self.user_name))
        self.b_1.place(x=20, y=200)

    def check_password(self, password, button, user_name):
        value_of_password = self.e_1.get().strip()
        cr.execute(f"select * from info where name = '{user_name}'")
        info = cr.fetchall()
        password = []
        for row in info:
            password.append(row[1])
        if int(value_of_password) == int(password[0]):
            if button == 'Deposit':
                deposit = Deposit(self, password, user_name)
            if button == 'Balance':
                balance = Balance(self, password, user_name)
            if button == 'Withdraw':
                withdraw = Withdraw(self, password, user_name)
        else:
            messagebox.showinfo("your password is wrong.\nplease, try again")

class Deposit:
    
    def __init__(self, main_window, password, user_name):
        self.window = Toplevel(main_window.window)
        self.window.geometry('600x770+340+100')
        self.window.title('ATM')
        icon = PhotoImage(file=r"d:\MSA\python projects\ATM\project code\photos\atm1.png")
        self.window.iconphoto(False, icon)
        self.window.resizable(False, False)
        self.window.configure(bg="#228B22")

        self.password = password
        self.user_name = user_name

        self.text_1 = Label(self.window, text='Deposit', fg='black', bg='#696969', font=("Bondi MT", 20))
        self.text_1.pack(fill= X)

        self.text_2 = Label(self.window, text='Enter money :', fg='black', bg='#228B22', font=("Bondi MT", 15))
        self.text_2.place(x= 15, y= 150)

        self.e_1 = Entry(self.window, font=("Bondi MT", 15), width=20, bg='#696969', fg='white')
        self.e_1.place(x= 225, y= 152)

        self.b_1 = Button(self.window, text='Check', fg='white', bg='#FFC125', width=31, font=("Bondi MT", 15), command=self.money_deposit)
        self.b_1.place(x= 20, y= 200) 

    def money_deposit(self):
        money = 0 
        cr.execute(f"select money from info where password = {self.password[0]}")
        for row in cr.fetchall():
            money = int(row[0])
        cr.execute(f"update info set money = {money + int(self.e_1.get())} where name = '{self.user_name}'")
        messagebox.showinfo('done')


class Balance:
    
    def __init__(self, main_window, password, user_name):
        self.window = Toplevel(main_window.window)
        self.window.geometry('600x770+340+100')
        self.window.title('ATM')
        icon = PhotoImage(file=r"d:\MSA\python projects\ATM\project code\photos\atm1.png")
        self.window.iconphoto(False, icon)
        self.window.resizable(False, False)
        self.window.configure(bg="#228B22")

        self.password = password
        self.user_name = user_name

        self.text_1 = Label(self.window, text='Balance', fg='black', bg='#696969', font=("Bondi MT", 20))
        self.text_1.pack(fill= X)

        self.text_2 = Label(self.window, text=self.money_balance(), fg='black', bg='#228B22', font=("Bondi MT", 15))
        self.text_2.pack(side='top')

    def money_balance(self):
        cr.execute(f"select * from info where name = '{self.user_name}'")
        for row in cr.fetchall():
            name = row[0]
            money = int(row[2])
        return f"Hello, {name}.\n you have {money} in the bank"

class Withdraw:

    def __init__(self, main_window, password, user_name):
        self.window = Toplevel(main_window.window)
        self.window.geometry('600x770+340+100')
        self.window.title('ATM')
        icon = PhotoImage(file=r"d:\MSA\python projects\ATM\project code\photos\atm1.png")
        self.window.iconphoto(False, icon)
        self.window.resizable(False, False)
        self.window.configure(bg="#228B22")

        self.password = password
        self.user_name = user_name

        self.text_1 = Label(self.window, text='Withdraw', fg='black', bg='#696969', font=("Bondi MT", 20))
        self.text_1.pack(fill= X)

        self.text_2 = Label(self.window, text='Enter money :', fg='black', bg='#228B22', font=("Bondi MT", 15))
        self.text_2.place(x= 15, y= 150)

        self.e_1 = Entry(self.window, font=("Bondi MT", 15), width=20, bg='#696969', fg='white')
        self.e_1.place(x= 225, y= 152)

        self.b_1 = Button(self.window, text='Check', fg='white', bg='#FFC125', width=31, font=("Bondi MT", 15), command=self.money_withdraw)
        self.b_1.place(x= 20, y= 200) 

    def money_withdraw(self):
        money = 0
        cr.execute(f"select money from info where name = '{self.user_name}'")
        for row in cr.fetchall():
            money = int(row[0])
        if int(self.e_1.get()) > money:
            messagebox.showinfo('Error', 'You don\'t have enough money')
        elif int(self.e_1.get()) < 100:
            messagebox.showinfo('Error', 'This amount is too small')
        else:
            cr.execute(f"update info set money = {money - int(self.e_1.get())} where name = '{self.user_name}'")
            messagebox.showinfo('Success', 'Withdrawal successful')

class Change_Password:
        
    def __init__(self, main_window, user_name, password, button):
        self.window = Toplevel(main_window.window)
        self.window.geometry('600x770+340+100')
        self.window.title('ATM')
        icon = PhotoImage(file=r"d:\MSA\python projects\ATM\project code\photos\atm1.png")
        self.window.iconphoto(False, icon)
        self.window.resizable(False, False)
        self.window.configure(bg="#228B22")

        self.password = password
        self.button = button
        self.code = self.message_of_code()
        self.user_name = user_name

        self.text_1 = Label(self.window, text='Change password', fg='black', bg='#696969', font=("Bondi MT", 20))
        self.text_1.pack(fill= X)

        self.text_2 = Label(self.window, text='I will send code for you.\nto check you are the user.\nthe message will take about 30 seconds', 
                            fg='black', bg='#228B22', font=("Bondi MT", 15))
        self.text_2.pack(side='top')

        self.b_1 = Button(self.window, text='send', fg='white', bg='#FFC125', width=31, font=("Bondi MT", 15),
                        command=lambda : self.send_message(self.code))
        self.b_1.place(x= 20, y= 200)

        self.text_3 = Label(self.window, text='Enter the code :', fg='black', bg='#228B22', font=("Bondi MT", 15))
        self.text_3.place(x=15, y=290)
        
        self.e_1 = Entry(self.window, font=("Bondi MT", 15), width=20, bg='#696969', fg='white')
        self.e_1.place(x=230, y=292)

        self.text_4 = Label(self.window, text='User name :', fg='black', bg='#228B22', font=("Bondi MT", 15))
        self.text_4.place(x=15, y=340)
        
        self.e_2 = Entry(self.window, font=("Bondi MT", 15), width=22, bg='#696969', fg='white')
        self.e_2.place(x=194, y=342)

        self.text_5 = Label(self.window, text='The new password :', fg='black', bg='#228B22', font=("Bondi MT", 15))
        self.text_5.place(x=15, y=390)
        
        self.e_3 = Entry(self.window, font=("Bondi MT", 15), width=17, bg='#696969', fg='white')
        self.e_3.place(x=282, y=392)  

        self.b_2 = Button(self.window, text='change', fg='white', bg='#FFC125', width=31, font=("Bondi MT", 15), command=self.change)
        self.b_2.place(x= 20, y= 460) 

    def message_of_code(self):
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

    def send_message(self, code):
        cr.execute(f"select * from info where name = '{self.user_name}'")
        phone = []
        for row in cr.fetchall():
            phone.append(row[3])
        current_hour = datetime.datetime.now().strftime('%H')
        current_min = datetime.datetime.now().strftime('%M')
        sendwhatmsg(f"+20{phone}", code, int(current_hour), int(current_min)+1)

    def change(self):
        new_password = self.e_3.get()
        if int(self.e_1.get().strip()) == int(self.code) and len(self.e_3.get()) == 4:
            cr.execute(f'UPDATE info SET password={str(new_password)} WHERE name="{self.e_2.get().strip()}"')
            messagebox.showinfo('the password is changed')
        else:
            messagebox.showinfo('the code is wrong')

main_window.window.mainloop()

