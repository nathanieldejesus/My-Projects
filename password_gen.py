from tkinter import *
import pyperclip
import random
import string

base = Tk()
base.geometry("400x250")
base.title("Password Generator")
pass_str = StringVar()
pass_len = IntVar()
pass_len.set(0)


def generate():
    # used to generate password from a list of characters selected randomly
    char_list = list(string.ascii_letters) + \
        list(string.digits) + list(string.punctuation)
    pass_list = []
    for i in range(pass_len.get()):
        pass_list.append(char_list[random.randint(0, len(char_list) - 1)])
    password = ''.join(pass_list)
    pass_str.set(password)


def copy():
    # uses pyperclip to allow for copying to clipboard
    my_pass = pass_str.get()
    pyperclip.copy(my_pass)


font = "SFPro 15 bold"
Label(base, text="Password Generator", font=font).pack()
Label(base, text="Password Length", font=font).pack(pady=3)
# box for entering password length
Entry(base, textvariable=pass_len).pack(pady=3)
# button to generate password
Button(base, text="Generate Password", command=generate).pack(pady=7)
# where the random password is generated
Entry(base, textvariable=pass_str).pack(pady=3)
# copies to clipboard
Button(base, text="Copy to Clipboard", command=copy).pack()
# infinite loop that keeps app running
base.mainloop()