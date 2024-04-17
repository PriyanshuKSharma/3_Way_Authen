import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cur = conn.cursor()

# Execute a SELECT query to fetch all rows from the userdata table
cur.execute("SELECT * FROM userdata")

# Fetch all rows from the cursor
rows = cur.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
