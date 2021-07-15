from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, sample
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [char for char in sample(letters, randint(8, 10))]
    symb_list = [symb for symb in sample(symbols, randint(2, 4))]
    num_list = [num for num in sample(numbers, randint(2, 4))]
    password_list = char_list + symb_list + num_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    web_site = (web_entry.get()).capitalize()
    username = username_entry.get()
    password = password_entry.get()
    new_entry = {
        web_site: {
            "username": username,
            "password": password,
        },
    }
    if len(web_site) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Error",
            message="Please don't leave any fields empty"
        )
    else:
        try:
            # check is the file exist
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            # create it if not
            with open("data.json", "w") as file:
                json.dump(new_entry, file, indent=4)
        else:
            # update or add new entry
            data.update(new_entry)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            # clear all the GUI fields
            web_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website = (web_entry.get()).capitalize()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if data[website]:
                s_username = data[website]["username"]
                s_password = data[website]["password"]
                messagebox.showinfo(
                    title=website,
                    message=f"Username: {s_username}\nPassword: {s_password}"
                )
    except KeyError:
        messagebox.showerror(
            title="Error",
            message=f"There is no information about {website}"
        )
    except FileNotFoundError:
        messagebox.showerror(
            title="Error",
            message="There is no database found"
        )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=33)
web_entry.grid(column=1, row=1, sticky="W")
web_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
gen_button = Button(text="Generate Password", command=create_password)
gen_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()

