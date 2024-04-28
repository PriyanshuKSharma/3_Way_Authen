import socket
import hashlib
import random

def generate_key():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))

def verify_login(username, password, key):
    # Add your verification logic here
    return username == "example" and password == "password" and key == "1234567890"

# Server setup
host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)  # Listen for only one connection

print("Server is listening for connections...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established.")

    # Generate one-time key
    one_time_key = generate_key()
    print("One-time key:", one_time_key)

    # Send one-time key to client
    client_socket.send(one_time_key.encode())

    # Receive username, password, and key from client
    username = client_socket.recv(1024).decode()
    password = client_socket.recv(1024).decode()
    key = client_socket.recv(1024).decode()

    # Verify login credentials
    login_result = "Login successful" if verify_login(username, password, key) else "Login failed"

    # Send login result back to client
    client_socket.send(login_result.encode())

    # Close client socket
    client_socket.close()