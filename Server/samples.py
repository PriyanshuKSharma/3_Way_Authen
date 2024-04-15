import sqlite3
import hashlib

conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute(''' 
            CREATE TABLE IF NOT EXISTS userdata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL
            )
            ''')

username1, password1 = "Joe Tribianni", hashlib.sha256("jt@friends".encode()).hexdigest()
username2, password2 = "Sheldon Cooper", hashlib.sha256("nerd@bigbang".encode()).hexdigest()
username3, password3 = "Raj K", hashlib.sha256("rk@bigbang".encode()).hexdigest()
username4, password4 = "Ross Gellar", hashlib.sha256("rg@friends".encode()).hexdigest()
username5, password5 = "Tony Stark", hashlib.sha256("ts@marvel".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username5, password5))

conn.commit()