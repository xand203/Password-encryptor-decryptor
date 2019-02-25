import json
from tkinter import *
from tkinter import messagebox
import tempfile
import time

with open('characters.json','r') as f:
    data = json.load(f)

encrypt_value = None
decrypt_value = None
key_value = None


def encrypt():
    password = encrypt_input.get()
    rd_password = ''
    total = 0
    characters = data["characters"]

    try:
        for number in key_value:
            total += int(number)
    except TypeError:
        messagebox.showwarning("WARNING","Insert a key!!")
    except ValueError:
        messagebox.showwarning("WARNING","Only use numbers for the key!!")

    for char in password:
        for p in characters:
            if char == p["char1"] or char == p["char1"].title():
                c = p["id"] + total
                n = data["characters"]
                while c > 35:
                    c -= 35
                d = characters[c]
                rd_password += d["char2"]
    global encrypt_value
    if encrypt_value:
        encrypt_value.destroy()
    encrypt_value = Label(master,text="Your encrypted password is: " + rd_password,fg="green",bg="yellow",font=("Comic Sans MS",12))
    encrypt_value.grid(row=3,column=1,pady=5,padx=5)


def decrypt():
    password = decrypt_input.get()
    rd_password = ''
    total = 0
    characters = data["characters"]

    try:
        for number in key_value:
            total += int(number)
    except TypeError:
        messagebox.showwarning("WARNING","Insert a key!!")
    except ValueError:
        messagebox.showwarning("WARNING","Only use numbers for the key!!")

    for char in password:
        for p in characters:
            if char == p["char2"] or char == p["char2"].title():
                c = p["id"] - total
                while c < 0:
                    c += 35
                d = characters[c]
                rd_password += d["char1"]

    global decrypt_value
    if decrypt_value:
        decrypt_value.destroy()

    decrypt_value = Label(master,text="Your decrypted password is: " + rd_password,fg="green",bg="yellow",font=("Comic Sans MS",12))
    decrypt_value.grid(row=5,column=1,pady=5,padx=5)

def getkey():
    global key_value
    key_value = key_input.get()

# Setup the GUI
master = Tk()
master.iconbitmap(r'lock_icon.ico')
master.title("Encrypt/Decrypt Aplication")
master.configure(background='yellow')



keyText = Label(master,text="Key Number",fg="green",bg="yellow",font=("Comic Sans MS",12))
keyText.grid(row=1,column=0,padx=5)
titleText = Label(master,text="ENCRYPT/DECRYPT PASSWORD",fg="green",bg="yellow",font=("Comic Sans MS",16))
titleText.grid(row=0,column=1,pady=5,padx=5)


key_input = Entry(master)
encrypt_input = Entry(master)
decrypt_input = Entry(master)


key_input.grid(row=1,column=1)
encrypt_input.grid(row=2,column=1)
decrypt_input.grid(row=4,column=1)

key_btn = Button(master,text="USE",command=getkey,bg='red')
encrypt_btn = Button(master, text="ENCRYPT", command=encrypt,bg='red')
decrypt_btn = Button(master, text="DECRYPT", command=decrypt,bg='red')

key_btn.grid(row=1,column=3,pady=5,padx=5)
encrypt_btn.grid(row=2,column=3,pady=5,padx=5)
decrypt_btn.grid(row=4,column=3,pady=5,padx=5)

mainloop( )
