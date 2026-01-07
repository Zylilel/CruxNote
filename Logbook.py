import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def logbook(user_email: str):
    cursor.execute("""
        SELECT username,
               max_f_grade,
               max_v_grade,
               finger_strength,
               pullup_strength
        FROM users
        WHERE email = ?
    """, (user_email.strip().lower(),))

    row = cursor.fetchone()
    if row is None:
        print("User not found.")
        return

    (username,
     max_f_grade,
     max_v_grade,
     finger_strength,
     pullup_strength) = row

    print(f"\nLogbook for {username} ({user_email}):\n")

    def print_entry(label, value):
        v = "Not recorded" if value is None else value
        print(f"{label}: {v}")

    print_entry("Max Font Grade", max_f_grade)
    print_entry("Max V Grade", max_v_grade)
    print_entry("Finger Strength (% BW)", finger_strength)
    print_entry("2RM Pull-Up Strength (% BW)", pullup_strength)

    input("Press Enter to return to the main menu...")
