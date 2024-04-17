import socket
import hashlib
import sqlite3

def verify_login(username, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    try:
        cur.execute("SELECT password FROM userdata WHERE username=?", (username,))
        stored_password = cur.fetchone()
        if stored_password and password == stored_password[0]:
            return "Login successful"
        else:
            return "Login failed"
    except Exception as e:
        print("Error:", e)
        return "Login failed"
    finally:
        conn.close()



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

    # Receive username and password from client
    data = client_socket.recv(1024).decode()
    print("Received data:", data)
    username, password = data.split(',')
    
    # Verify login credentials
    login_result = verify_login(username, password)

    # Send login result back to client
    client_socket.send(login_result.encode())

    # Close client socket if login failed
    if login_result == "Login failed":
        client_socket.close()
