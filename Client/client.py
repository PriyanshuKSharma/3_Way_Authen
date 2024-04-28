import tkinter as tk
import socket

def authenticate():
    username = username_entry.get()
    password = password_entry.get()
    otp = otp_entry.get()  # Get the entered one-time password

    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send username, password, and OTP to server
    client_socket.send(username.encode())
    client_socket.send(password.encode())
    client_socket.send(otp.encode())  # Send OTP to the server

    # Receive login result from server
    login_result = client_socket.recv(1024).decode()

    # Close client socket
    client_socket.close()

    # Update GUI based on login result
    if login_result.startswith("Login successful"):
        result_label.config(text=login_result)
    else:
        result_label.config(text=login_result)

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

# Hide the OTP entry widget
otp_label = tk.Label(root, text="One-time Password:")
otp_label.grid(row=2, column=0, padx=10, pady=5)
otp_entry = tk.Entry(root, show="*")  # Show the entry widget but with a password mask
otp_entry.grid(row=2, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="Login", command=authenticate)
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
