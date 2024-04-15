import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen()

def handle_connection(c):
    c.send("Enter username:".encode())
    username = c.recv(1024).decode()
    c.send("Enter password:".encode())
    password = c.recv(1024).decode()
    password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('users.db')  # Corrected database name
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE username=? AND password=?", (username, password))  # Corrected table name

    if cur.fetchall():
        c.send("Login successful".encode())
    else:
        c.send("Login failed".encode())

    c.close()  # Close connection after handling

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()
