import tkinter as tk
import socket
import hashlib

def generate_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate():
    username = username_entry.get()
    password = password_entry.get()
    password_hash = generate_hash(password)  # Generate hash for the password
    
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    data = username + ',' + password_hash  # Send username and password hash
    client_socket.send(data.encode())

    response = client_socket.recv(1024).decode()
    result_label.config(text=response)

    client_socket.close()


# GUI setup
root = tk.Tk()
root.title("Client")

username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="Login", command=authenticate)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
