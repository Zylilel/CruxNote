import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def ensure_user(email):
    cursor.execute("INSERT OR IGNORE INTO users (email) VALUES (?)", (email,))
    conn.commit()

def update_user(email, data):
    keys = ", ".join([f"{k} = ?" for k in data.keys()])
    vals = list(data.values()) + [email]
    cursor.execute(f"UPDATE users SET {keys} WHERE email = ?", vals)
    conn.commit()

def recfingerworkout():
    print("\nRecommended Finger Strength Workouts:")
    print("- 7/3 Repeaters on 20mm edge (4 sets of 6 reps)")
    print("- Max Hangs with added weight (5 reps, 10 seconds each)")
    print("- Density hangs for 30s if you're just starting out")
    print("- Limit bouldering 1x per week on steep boards")

def recpullworkout():
    print("\nRecommended Pull-Up Strength Workouts:")
    print("- Weighted pull-ups: 3–5 sets of 3–5 reps")
    print("- 1-arm negatives or assisted 1-arm pull-ups")
    print("- Bodyweight pull-ups to failure")
    print("- Limit bouldering for pulling power")

fgrademaxhang = [
    ["6A", 90, 110, 130], ["6B", 100, 120, 140], ["6C", 105, 125, 145],
    ["7A", 110, 130, 150], ["7B", 115, 135, 155], ["7C", 120, 140, 160],
    ["8A", 125, 145, 165], ["8B", 130, 150, 170], ["8C", 135, 155, 175],
    ["9A", 140, 160, 180], ["9B", 145, 165, 185], ["9C", 150, 170, 190]
]

vgrademaxhang = [
    ["V1", 70, 90, 110], ["V2", 80, 100, 120], ["V3", 90, 110, 130],
    ["V4", 100, 120, 140], ["V5", 105, 125, 145], ["V6", 110, 130, 150],
    ["V7", 115, 135, 155], ["V8", 120, 140, 160], ["V9", 125, 145, 165],
    ["V10", 130, 150, 170], ["V11", 135, 155, 175], ["V12", 140, 160, 180],
    ["V13", 145, 165, 185], ["V14", 150, 170, 190], ["V15", 155, 175, 195],
    ["V16", 160, 180, 200], ["V17", 165, 185, 205], ["V18", 170, 190, 210]
]

fgrade2rm = [
    ["6A", 60, 80, 100], ["6B", 70, 90, 110], ["6C", 80, 100, 120],
    ["7A", 90, 110, 130], ["7B", 100, 120, 140], ["7C", 110, 130, 150],
    ["8A", 120, 140, 160], ["8B", 130, 150, 170], ["8C", 140, 160, 180],
    ["9A", 150, 170, 190], ["9B", 160, 180, 200], ["9C", 170, 190, 210]
]

vgrade2rm = [
    ["V1", 70, 90, 110], ["V2", 80, 100, 120], ["V3", 85, 105, 125],
    ["V4", 90, 110, 130], ["V5", 95, 115, 135], ["V6", 100, 120, 140],
    ["V7", 105, 125, 145], ["V8", 110, 130, 150], ["V9", 115, 135, 155],
    ["V10", 120, 140, 160], ["V11", 125, 145, 165], ["V12", 130, 150, 170],
    ["V13", 135, 155, 175], ["V14", 140, 160, 180], ["V15", 145, 165, 185],
    ["V16", 150, 170, 190], ["V17", 155, 175, 195], ["V18", 160, 180, 200]
]

def strengthsandweaknesses(user_email):
    user_email = user_email.strip().lower()
    ensure_user(user_email)

    while True:
        grading = input("Choose grading system (F for Font / V for V-Grade):\n- ").strip().lower()
        if grading in ("f", "v"):
            break
        print("Please enter 'F' or 'V'.")

    selected_grade = input("Enter your climbing grade (e.g. 7A or V5):\n- ").strip().upper()
    grading_data = fgrademaxhang if grading == "f" else vgrademaxhang

    update_user(user_email, {"max_f_grade" if grading == "f" else "max_v_grade": selected_grade})

    print("\nFinger Strength Test")
    while True:
        x = input("Enter your finger strength result (% bodyweight):\n- ").strip()
        if x.replace(".", "", 1).isdigit():
            percent = float(x)
            if 0 < percent < 300:
                break
            print("Please enter a realistic value (e.g. 90–220).")
        else:
            print("Please enter a valid number (e.g. 135.5).")

    update_user(user_email, {"finger_strength": percent})

    found = False
    for g, low, mid, high in grading_data:
        if g.lower() == selected_grade.lower():
            print(f"\nFor grade {g}:")
            print(f"- Weak:    {low}%")
            print(f"- Average: {mid}%")
            print(f"- Strong:  {high}%")
            print(f"\nYour result: {percent}%")
            if percent < low:
                print("Your finger strength is below expected.")
                recfingerworkout()
            elif percent < mid:
                print("Slightly below average — there's room to improve.")
                recfingerworkout()
            elif percent <= high:
                print("You're in the expected range or slightly stronger than average.")
            else:
                print("Excellent! Your finger strength is above average.")
            found = True
            break
    if not found:
        print("Could not find your grade in the data.")

    print("\nPull-Up Strength Test")
    while True:
        y = input("Enter your pull-up strength result (% bodyweight):\n- ").strip()
        if y.replace(".", "", 1).isdigit():
            pull_percent = float(y)
            if 0 < pull_percent < 300:
                break
            print("Please enter a realistic percentage (e.g. 70–250).")
        else:
            print("Please enter a valid number (e.g. 135.5).")

    update_user(user_email, {"pullup_strength": pull_percent})

    pullup_data = fgrade2rm if grading == "f" else vgrade2rm
    for g, low, mid, high in pullup_data:
        if g.lower() == selected_grade.lower():
            print(f"\nFor grade {g}:")
            print(f"- Weak:    {low}%")
            print(f"- Average: {mid}%")
            print(f"- Strong:  {high}%")
            print(f"\nYour pull-up result: {pull_percent}%")
            if pull_percent < low:
                print("Your pull-up strength is below expected.")
                recpullworkout()
            elif pull_percent < mid:
                print("Slightly below average — there's room to improve.")
                recpullworkout()
            elif pull_percent <= high:
                print("You're in the expected range or slightly stronger than average.")
            else:
                print("Excellent! Your pull-up strength is above average.")
            break

    input("\nPress Enter to return...\n- ")
