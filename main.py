from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 8))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email_username = email_username_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as password_file:
                #Reading old data
                data = json.load(password_file)
        except FileNotFoundError:
            with open("data.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as password_file:
                #Saving updated data
                json.dump(data, password_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_search = website_entry.get()
    #Check if user's text entry matches an item in the data.json
    try:
        with open("data.json", "r") as password_file:
            password_data = json.load(password_file)
            if website_search in password_data:
                email = password_data[website_search]["email"]
                password = password_data[website_search]['password']
                messagebox.showinfo(title=website_search, message=f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website_search in password_data:
            email = password_data[website_search]["email"]
            password = password_data[website_search]['password']
            messagebox.showinfo(title=website_search, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_search} exists.")

# ---------------------------- UI SETUP ------------------------------- #


login_window = Tk()
login_window.title("Login")
login_window.config(padx=50, pady=50, bg="white")

login_label = Label(text="Login to your account", bg="white", fg="black", font=("Courier",35, "bold"))
login_label.grid(row=0, column=1)

email_address_label = Label(text="Email: ", bg="white", fg="black")
email_address_label.grid(row=2, column=0)

email_address_entry = Entry(bg="white", fg="black", highlightthickness=0, width=35)
email_address_entry.grid(row=2, column=1)

password_label = Label(text="Password: ", bg="white", fg="black")
password_label.grid(row=4, column=0)

password_entry = Entry(bg="white", fg="black", highlightthickness=0, width=35)
password_entry.grid(row=4, column=1)

sign_in_button = Button(text="Sign In", highlightbackground="white", width=28)
sign_in_button.grid(row=6,column=1)


login_window.mainloop()

# ---------------------------- UI SETUP ------------------------------- #


password_manager_window = Tk()
password_manager_window.title("Password Manager")
password_manager_window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white", fg="black")
website_label.grid(column=0, row=1, )

website_entry = Entry(bg="white", fg="black", highlightthickness=0, width=20)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=1)

search_button = Button(text="Search", highlightbackground="white", width=10, command=find_password)
search_button.grid(column=2, row=1)

email_username_label = Label(text="Email/Username:", bg="white", fg="black")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(bg="white", fg="black", highlightthickness=0, width=35)
email_username_entry.insert(0, "cchima1014@yahoo.com", )
email_username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", bg="white", fg="black")
password_label.grid(column=0, row=3)

password_entry = Entry(bg="white", fg="black", highlightthickness=0, width=20)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", highlightbackground="white", width=10,
                                  command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightbackground="white", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

password_manager_window.mainloop()
