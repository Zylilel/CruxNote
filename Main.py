from Register import register
from Login import login
from Workout import workout
from StrengthsAndWeaknesses import strengthsandweaknesses
from Logbook import logbook
from Techniques import techniques

while True:
    print("Welcome to CruxNotes!")
    choice = input("Do you want to (L)Login, (R)Register or (E)Exit?: ").strip().lower()

    if choice == "l":
        logged_in_email = login()
        if logged_in_email:
            break
    elif choice == "r":
        register()
    elif choice == "e":
        print("Goodbye!")
        exit()
    elif choice == "admin":
        logged_in_email = "admin@gmail.com"
        break
    else:
        print("Please enter a valid choice.")

while True:
    option = input(
        "What are you interested in?\n"
        "(1) Workouts\n"
        "(2) Strengths and Weaknesses\n"
        "(3) Logbook\n"
        "(4) Techniques\n"
        "(E) Exit\n- "
    ).strip()

    if option == "1":
        workout()
    elif option == "2":
        strengthsandweaknesses(logged_in_email)
    elif option == "3":
        logbook(logged_in_email)
    elif option == "4":
        techniques()
    elif option.lower() == "e":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid choice.")
