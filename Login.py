import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def login():
    attempt = 0

    while True:
        email = input("Please enter your email: ").strip().lower()

        cursor.execute("SELECT username, password FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()

        if row is None:
            print("Invalid email. Please enter again.")
            continue

        username, stored_password = row

        while True:
            password_input = input("Please enter your password: ").strip()

            if password_input == stored_password:
                print("Welcome", username)
                return email

            print("Invalid password. Please try again.")
            attempt += 1

            if attempt >= 3:
                reset = input("Do you want to reset your password? (Y/N): ").strip().lower()
                if reset == "y":
                    while True:
                        new_pass = input("Enter a new password: ").strip()
                        if len(new_pass) < 8:
                            print("Password must be longer than 7 characters.")
                        elif not any(char.isdigit() for char in new_pass):
                            print("Password must contain a number.")
                        elif "," in new_pass:
                            print("Password cannot contain commas.")
                        else:
                            cursor.execute(
                                "UPDATE users SET password = ? WHERE email = ?",
                                (new_pass, email)
                            )
                            conn.commit()
                            print("Password successfully updated. Please login again.")
                            return None
                else:
                    print("Try logging in again.")
                    attempt = 0
                    break
