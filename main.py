from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    web_site = web_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    with open("data.txt", mode="a") as file:
        file.write(
            f"\n{web_site} | {username} | {password}"
        )
    web_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


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
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
web_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
gen_button = Button(text="Generate Password")
gen_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()

