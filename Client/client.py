import socket
import tkinter as tk
from tkinter import messagebox

def login(username, password):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5500))
    client_socket.send(username.encode())
    client_socket.send(password.encode())
    response = client_socket.recv(1024).decode()
    messagebox.showinfo("Login Result", response)
    client_socket.close()

def submit_login():
    username = entry_username.get()
    password = entry_password.get()
    login(username, password)

# GUI Setup
root = tk.Tk()
root.title("Login")
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()
label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()
button_login = tk.Button(root, text="Login", command=submit_login)
button_login.pack()
root.mainloop()
