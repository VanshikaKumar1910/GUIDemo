from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def handle_login():
    email = email_input.get()
    password = password_input.get()

    if not email or not password:
        messagebox.showwarning("Input Error",
                               "Please enter both email and password")
        return

    print(email, password)


def toggle_password():
    if password_input.cget('show') == '':
        password_input.config(show='*')
        toggle_btn.config(text='Show Password')
    else:
        password_input.config(show='')
        toggle_btn.config(text='Hide Password')


def forgot_password():
    messagebox.showinfo(
        "Forgot Password",
        "Password reset instructions have been sent to your email.")


def sign_up():
    messagebox.showinfo("Sign Up", "Redirecting to the sign-up page...")


root = Tk()

root.title('Login Form')

root.geometry('500x700')
root.configure(background='#F0F8FF')  # Light Alice Blue background

img = Image.open('waranya-mooldee-Efj0HGPdPKs-unsplash.jpg')
resized_img = img.resize((120, 120))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img, background='#F0F8FF')
img_label.pack(pady=(20, 10))

text_label = Label(root,
                   text='Welcome to Bunny',
                   fg='#333333',
                   bg='#F0F8FF',
                   font=('Verdana', 26))
text_label.pack(pady=(20, 10))

email_label = Label(root,
                    text='Enter Email:',
                    fg='#333333',
                    bg='#F0F8FF',
                    font=('Verdana', 16))
email_label.pack()
email_input = Entry(root, width=50, font=('Verdana', 12))
email_input.pack(ipady=6, pady=(5, 15))

password_label = Label(root,
                       text='Enter Password:',
                       fg='#333333',
                       bg='#F0F8FF',
                       font=('Verdana', 16))
password_label.pack()
password_input = Entry(root, width=50, font=('Verdana', 12), show='*')
password_input.pack(ipady=6, pady=(5, 15))

toggle_btn = Button(root,
                    text='Show Password',
                    fg='white',
                    bg='#007BFF',
                    font=('Verdana', 10),
                    command=toggle_password)
toggle_btn.pack(pady=(5, 15))

login_btn = Button(root,
                   text='Login Here',
                   fg='white',
                   bg='#007BFF',
                   width=20,
                   height=2,
                   command=handle_login,
                   font=('Verdana', 12),
                   relief=RAISED)
login_btn.pack(pady=(10, 20))

forgot_btn = Button(root,
                    text='Forgot Password?',
                    fg='#007BFF',
                    bg='#F0F8FF',
                    font=('Verdana', 10),
                    command=forgot_password,
                    relief=FLAT)
forgot_btn.pack(pady=(5, 10))

sign_up_btn = Button(root,
                     text='Sign Up',
                     fg='white',
                     bg='#28A745',
                     font=('Verdana', 12),
                     command=sign_up,
                     relief=RAISED)
sign_up_btn.pack(pady=(10, 20))

root.mainloop()
