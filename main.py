from tkinter import messagebox
from tkinter import *
import random

import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate():
    global password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_symbol + password_number + password_letter

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)




# ---------------------------- FIND DATA ------------------------------- #
def find():
    website = website_input.get()
    with open("data.json")as data_files:
        data = json.load(data_files)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Data", message=f"email:{email}\n password:{password}")
            website_input.delete(0, 'end')

        else:
            messagebox.showinfo(title="Data", message="There is no such Field ")
            website_input.delete(0, 'end')


# ---------------------------- SAVE DATA ------------------------------- #

def save():
    website = website_input.get()
    email = Email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title="Oops!", message="Please Fill all the fields ")
    else:
        try:
            with open("data.json", "r") as data_files:
                # reading old data
                data = json.load(data_files)
                # updating old data with new data
                data.update(new_data)
            with open("data.json", "w")as data_files:
                # saving updated data
                json.dump(data, data_files, indent=4)


        except FileNotFoundError:
            with open("data.json", "w")as data_files:
                # saving updated data
                json.dump(new_data, data_files, indent=4)

        finally:
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')




def validateLogin():


    user_pass = Pass_Entry.get()
    user_name = Id_Entry.get()
    if user_name == '' or user_pass == '':
        print("fill the empty field!!!")
    else:
        if user_name == "Achyutam" and user_pass == "qwerty":

            messagebox.showinfo(title="Hurray!", message="Login Successful ")
            Id_Entry.config(highlightbackground="green", highlightcolor="green")
            Pass_Entry.config(highlightbackground="green", highlightcolor="green")
            Login_button.config(bg="#81B214", fg="#CDC733")
            Login_button.config(state="disable")
            Id_Entry.delete(0, 'end')
            Pass_Entry.delete(0, 'end')
            Id_Entry.config(state="disable")
            Pass_Entry.config(state="disable")

            working()

        else:
            messagebox.askokcancel(title="Oops!", message="Wrong username and password ")
            Id_Entry.delete(0, 'end')
            Pass_Entry.delete(0, 'end')


# ------------------------Login page ---------------------#

def Login():
    global Id_Entry, Pass_Entry, Login_button

    Id_Label = Label()
    Id_Label.config(text="ID  : ", bg="white", highlightthickness=2)
    Id_Label.grid(row=5, column=0, padx=5, pady=5)

    Id_Entry = Entry(width=60, bg="white", highlightthickness=2, highlightbackground="red", highlightcolor="red")
    Id_Entry.focus()
    Id_Entry.grid(row=5, column=1, columnspan=2)

    Pass_label = Label()
    Pass_label.config(text="Password : ", bg="white", highlightthickness=2)
    Pass_label.grid(row=6, column=0, padx=5, pady=5)

    Pass_Entry = Entry(width=60, bg="white", highlightthickness=2, highlightbackground="red", highlightcolor="red")
    Pass_Entry.grid(row=6, column=1, columnspan=2)

    # login button
    Login_button = Button(text="LogIn", width=51, bg="orange", highlightthickness=0, command=validateLogin)
    Login_button.grid(row=7, column=1, columnspan=2, pady=5)


def working():
    global website_text, website_input, Email_text, Email_input, password_text, password_input, add_button
    # ------------------------Website---------------------#
    website_text = Label()
    website_text.config(text="Website  : ", bg="white", highlightthickness=0)
    website_text.grid(row=1, column=0, padx=5, pady=5)

    website_input = Entry(width=35, bg="white", highlightthickness=0)
    website_input.focus()
    website_input.grid(row=1, column=1)

    search_button = Button(text="Search", width=20, bg="orange", command=find)
    search_button.grid(row=1, column=2)

    # ------------------------Email---------------------#
    Email_text = Label()
    Email_text.config(text="Email/UserName  : ", bg="white", highlightthickness=0)
    Email_text.grid(row=2, column=0, padx=5, pady=5)

    Email_input = Entry(width=60, bg="white", highlightthickness=0)
    Email_input.insert(END, "@gmail.com")
    Email_input.grid(row=2, column=1, columnspan=2)

    # ------------------------Password---------------------#
    password_text = Label()
    password_text.config(text="Password  : ", bg="white", highlightthickness=0)
    password_text.grid(row=3, column=0, padx=5, pady=5)
    password_input = Entry()
    password_input.config(width=35, bg="white", highlightthickness=0)
    password_input.grid(row=3, column=1)

    button = Button(text="Generate Password", width=20, bg="orange", highlightthickness=0, command=generate)
    button.grid(row=3, column=2, pady=5)

    add_button = Button(text="Add", width=51, bg="orange", highlightthickness=0, command=save)
    add_button.grid(row=4, column=1, columnspan=2, pady=5)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg="white")


canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=img)
canvas.config(bg="white", highlightthickness=0)
canvas.grid(row=0, column=1)
Login()

window.mainloop()
