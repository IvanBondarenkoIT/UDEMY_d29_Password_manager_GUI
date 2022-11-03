import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

FONT = ("Arial", 12)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, 'end')
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if not website or not password:
        messagebox.showinfo(title="Ooops!", message="You have empty entries")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There is a details:\n Email:{email}\nPassword{password}"
                                                              f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                text = f"{website} | {email} | {password}\n"
                file.write(text)
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)
# canvas
logo_img = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# labels
# Website:
website_lab = tk.Label(text="Website:", font=FONT)
website_lab.grid(column=0, row=1)
# Email/Username:
email_lab = tk.Label(text="Email/Username:", font=FONT)
email_lab.grid(column=0, row=2)
# Password:
password_lab = tk.Label(text="Password:", font=FONT)
password_lab.grid(column=0, row=3)
# entries
# Website:
website_input = tk.Entry(width=51)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
# Email/Username:
email_input = tk.Entry(width=51)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "myemail@gmail.com")
# Password:
password_input = tk.Entry(width=21)
password_input.grid(column=1, row=3)
# buttons
# Generate Password
generate_password_button = tk.Button(text="Generate Password", command=generate_password, highlightthickness=0)
generate_password_button.grid(column=2, row=3)
# Add
add_button = tk.Button(text="Add", width=43, command=add_button, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
