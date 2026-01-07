import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def register():

    while True:
        email = input("Please enter an email: ").strip().lower()
        if "@" in email and "." in email and "," not in email:
            cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
            if cursor.fetchone():
                print("Email already registered. Please use another email.")
            else:
                break
        else:
            print("Invalid email. Please enter again.")

    while True:
        password = input("Please enter a password: ").strip()
        if len(password) < 8:
            print("Password must be longer than 7 characters.")
        elif not any(char.isdigit() for char in password):
            print("Password must contain a number.")
        elif "," in password:
            print("Password cannot contain commas.")
        else:
            break

    while True:
        username = input("Please enter a username: ").strip()
        if username == "":
            print("Username cannot be empty.")
        else:
            break

    cursor.execute("INSERT INTO users (email, password, username) VALUES (?, ?, ?)", (email, password, username))
    conn.commit()
    print("Registration complete.")