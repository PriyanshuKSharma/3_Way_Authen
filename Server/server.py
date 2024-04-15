import socket
import sqlite3
import hashlib

def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT password FROM userdata WHERE username=?", (username,))
    result = cur.fetchone()
    conn.close()
    if result:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password == result[0]
    return False

def handle_client(client_socket):
    while True:
        username = client_socket.recv(1024).decode()
        password = client_socket.recv(1024).decode()
        if authenticate(username, password):
            client_socket.send("Login successful".encode())
        else:
            client_socket.send("Invalid credentials".encode())

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5500))
    server_socket.listen(5)
    print("Server listening...")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
