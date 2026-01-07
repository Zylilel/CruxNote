def workout():
    while True:
        print("\nWelcome to the workout")
        print("Choose your workout type based on your goals:")
        print("(1) Endurance")
        print("(2) Power Endurance")
        print("(3) Strength & Power")
        print("(4) Conditioning")
        print("(q) Quit")

        workoutoption = input("Please enter your choice: ").strip().lower()

        if workoutoption == "1":
            endurance()
        elif workoutoption == "2":
            powerendurance()
        elif workoutoption == "3":
            strengthandpower()
        elif workoutoption == "4":
            conditioning()
        elif workoutoption == "q":
            print("See you!")
            break
        else:
            print("Invalid input. Please try again.")

def endurance():
    while True:
        print("Endurance refers to the climber's ability to sustain moderate intensity climbing for an extended period.\nThis can help you to fight the pump while climbing and is very useful for activities like lead climbing.")
        print("Choose a specific endurance workout:")
        print("(1) ARC Training")
        print("(2) Low-Intensity Circuits")
        print("(3) Repeaters on Easy Routes")
        print("(4) Hangboard Recovery Repeaters")
        print("(b) Back to main menu")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            arc_training()
        elif choice == "2":
            low_intensity_circuits()
        elif choice == "3":
            repeaters_easy_routes()
        elif choice == "4":
            hangboard_recovery_repeaters()
        elif choice == "b":
            break
        else:
            print("Invalid input. Please try again.")

def powerendurance():
    while True:
        print("Power Endurance refers to the climber’s ability to repeatedly perform powerful movements or sequences on a route, without significantly losing strength or efficiency due to fatigue. This can help you sustain near maximum efficiency without being fatigued and can be very useful for hard bouldering.")
        print("Choose a specific power endurance workout:")
        print("(1) Hangboard Repeaters")
        print("(2) Boulder Circuit")
        print("(3) Linked Boulder")
        print("(b) Back to main menu")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            hangboard_repeaters()
        elif choice == "2":
            boulder_circuit()
        elif choice == "3":
            linked_boulder()
        elif choice == "b":
            break
        else:
            print("Invalid input. Please try again.")

def strengthandpower():
    while True:
        print("Strength & Power refers to the ability to exert the maximum force a climber can exert quickly and explosively. This can help you to improve your general strengths, finger strength, and explosiveness.")
        print("Choose a specific strength and power workout:")
        print("(1) Max Hangs - 90%")
        print("(2) Board 10")
        print("(3) Limit Bouldering")
        print("(4) Max Hangs - One Arm 90%")
        print("(5) Pinch Block Max 90%")
        print("(6) Small Edges 10mm - 70%")
        print("(7) Boulder Campus")
        print("(8) Campus Latches")
        print("(9) Limit Power - Intermediate")
        print("(b) Back to main menu")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            max_hangs_90()
        elif choice == "2":
            board_10()
        elif choice == "3":
            limit_bouldering()
        elif choice == "4":
            one_arm_max_hangs()
        elif choice == "5":
            pinch_block()
        elif choice == "6":
            small_edges()
        elif choice == "7":
            boulder_campus()
        elif choice == "8":
            campus_latches()
        elif choice == "9":
            limit_power()
        elif choice == "b":
            break
        else:
            print("Invalid input. Please try again.")

def conditioning():
    while True:
        print("Conditioning refers to physical training designed to improve a climber's overall fitness and performance, encompassing strength, endurance, flexibility, and other related aspects. This can help you to perform techniques with better accuracy and efficiency.")
        print("Choose a specific conditioning workout:")
        print("(1) Deadlift")
        print("(2) Bar Core")
        print("(3) Bench Press")
        print("(4) Weighted Pull-ups - 85%")
        print("(5) On the Minute Pull-ups")
        print("(6) One-arm Assisted Pull-ups")
        print("(b) Back to main menu")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "1":
            deadlift()
        elif choice == "2":
            bar_core()
        elif choice == "3":
            bench_press()
        elif choice == "4":
            weighted_pullups()
        elif choice == "5":
            on_the_minute()
        elif choice == "6":
            one_arm_assisted()
        elif choice == "b":
            break
        else:
            print("Invalid input. Please try again.")

def arc_training():
    print("\n--- ARC Training (Aerobic Restoration & Capillarity) ---")
    print("Goal: Build aerobic base and capillary density by climbing at low intensity for a long time.\n")
    print("Warm-up:")
    print("- 10–15 minutes of light climbing and shoulder mobility")
    print("\nWorkout:")
    print("- Climb continuously on easy route (about 2-3 grades below your max)")
    print("- Total time-on-wall: 30–45 minutes")
    print("- Break into 2–3 sets (e.g., 3 × 15 min)")
    print("- Rest 5–10 minutes between sets")
    print("- Focus on relaxed, smooth movements; avoid getting pumped")
    input("\nPress Enter to return...")

def low_intensity_circuits():
    print("\n--- Low-Intensity Circuits ---")
    print("Goal: Build endurance using a loop of easy problems with continuous movement.\n")
    print("Setup:")
    print("- Choose 4–6 easy problems (around 2-3 grades below max)")
    print("- Link them into a circuit you can climb repeatedly")
    print("\nWorkout:")
    print("- Climb the circuit for 10–15 minutes continuously")
    print("- Maintain steady breathing and rhythm")
    print("- Keep intensity light and sustainable")
    print("- Do 2–3 total circuits with 5–10 minutes rest between")
    input("\nPress Enter to return...")

def repeaters_easy_routes():
    print("\n--- Repeaters on Easy Routes ---")
    print("Goal: Build volume and fluency through repeated, low-intensity climbing.\n")
    print("Setup:")
    print("- Choose an easy route or boulder problem you can climb repeatedly without much effort")
    print("\nWorkout:")
    print("- Climb it 2-5 times in a row")
    print("- Rest 10–30 seconds between reps")
    print("- Perform 3–5 total sets")
    print("- Rest 3–5 minutes between sets")
    print("- Stay below pump threshold, focus on technique and breathing")
    input("\nPress Enter to return...")

def hangboard_recovery_repeaters():
    print("\n--- Hangboard Recovery Repeaters ---")
    print("Goal: Gently load the fingers to stimulate blood flow without fatigue. Ideal for recovery days or maintaining tendon health.\n")
    print("Setup:")
    print("- Use a 20–25mm flat edge (comfortable grip)")
    print("- No added weight; just bodyweight")
    print("- Timer or stopwatch required\n")
    print("Workout:")
    print("- Hang for 7 seconds")
    print("- Rest for 3 seconds")
    print("- Repeat 5–6 times per set")
    print("- Complete 3 sets total")
    print("- Rest 1–2 minutes between sets\n")
    input("\nPress Enter to return...")

def hangboard_repeaters():
    print("\n--- Hangboard Repeaters ---")
    print("Goal: Improve the forearm's power endurance for shorter intense sections of climbing.")
    print("Setup:")
    print("- Choose an edge you can hang comfortably at ~60–70% max effort")
    print("Workout:")
    print("- Hang for 7 sec, rest for 3 sec")
    print("- Repeat for 6–7 reps")
    print("- Rest 2–3 minutes")
    print("- Do 3–5 sets total")
    input("\nPress Enter to return...")

def boulder_circuit():
    print("\n--- Boulder Circuit ---")
    print("Goal: Develop sustained strength on moderately hard sequences.")
    print("Setup:")
    print("- Choose 4–6 boulder problems ~80% max effort")
    print("- Link them together with minimal rest")
    print("Workout:")
    print("- Climb circuit continuously for 30–60 seconds")
    print("- Rest 2–4 minutes")
    print("- Do 4–6 total sets")
    input("\nPress Enter to return...")

def linked_boulder():
    print("\n--- Linked Boulder Problems ---")
    print("Goal: Increase short power endurance for short routes, crux sequences or longer boulder problems.")
    print("Setup:")
    print("- Choose 1-3 problems close in location at around flash grade")
    print("Workout:")
    print("- Climb all consecutively with minimal rest.")
    print("- Total effort time: 30–60 sec")
    print("- Rest 4-5 min between sets")
    print("- Do 3-4 sets")
    input("\nPress Enter to return...")

def max_hangs_90():
    print("\n--- Max Hangs - 90% ---")
    print("Goal: Improve finger strength at high intensity.")
    print("Setup: 20mm edge, 90% of max total load.")
    print("Workout:")
    print("- 6 sets of 1x10 sec hang")
    print("- Full recovery between sets")
    print("- Adjust weight so you can complete the full hang without form breakdown")
    input("\nPress Enter to return...")

def board_10():
    print("\n--- Board 10 ---")
    print("Goal: Develop full-body climbing power and coordination.")
    print("Setup: Training board.")
    print("Workout:")
    print("- 5 warm-up problems (moderate, max 2 attempts)")
    print("- 5 near-limit problems (max 4 attempts per problem)")
    print("- Rest as needed to maintain performance")
    input("\nPress Enter to return...")

def limit_bouldering():
    print("\n--- Limit Bouldering ---")
    print("Goal: Build max strength and coordination.")
    print("Setup: Hard boulders near your maximum effort.")
    print("Workout:")
    print("- Choose 3–5 problems")
    print("- Max 3 attempts per problem")
    print("- Rest 3–5 minutes between attempts")
    input("\nPress Enter to return...")

def one_arm_max_hangs():
    print("\n--- Max Hangs - One Arm 90% ---")
    print("Goal: Develop unilateral finger strength.")
    print("Setup: 20mm edge, one-arm hang, use pulley to reduce weight.")
    print("Workout:")
    print("- 6 sets of 1x10 sec hang per arm")
    print("- 30 sec rest between arms")
    print("- Full rest between sets")
    input("\nPress Enter to return...")

def pinch_block():
    print("\n--- Pinch Block Max 90% ---")
    print("Goal: Increase pinch grip strength.")
    print("Setup: Pinch block, 90% of your max load.")
    print("Workout:")
    print("- 6 sets of 10 sec pinch hangs")
    print("- Reduce load if full hang is not possible")
    print("- Use proper lifting technique")
    input("\nPress Enter to return...")

def small_edges():
    print("\n--- Small Edges 10mm - 70% ---")
    print("Goal: Improve finger strength on small holds.")
    print("Setup: 10mm edge, 70% intensity or RPE 7/10.")
    print("Workout:")
    print("- 5 hangs at 10 sec each")
    print("- Warm-up progressively to training edge size")
    print("- Adjust weight to match intensity")
    input("\nPress Enter to return...")

def boulder_campus():
    print("\n--- Boulder Campus ---")
    print("Goal: Build upper-body pulling power.")
    print("Setup: Overhung boulder problems done without feet.")
    print("Workout:")
    print("- Use 4 problems")
    print("- No matching unless required")
    print("- 3 min rest between attempts")
    print("- Focus on big dynamic movements")
    input("\nPress Enter to return...")

def campus_latches():
    print("\n--- Campus Latches ---")
    print("Goal: Train one-arm explosive contact strength.")
    print("Setup: Campus board.")
    print("Workout:")
    print("- Jump and latch with one arm for 1–2 seconds")
    print("- 3 reps per arm, 3 sets total")
    print("- 2 min rest between sets")
    input("\nPress Enter to return...")

def limit_power():
    print("\n--- Limit Power - Intermediate ---")
    print("Goal: Improve arm and upper body power.")
    print("Setup: Campus board, smallest usable rung.")
    print("Workout:")
    print("- Sets 1-4: 1-2-3")
    print("- Sets 5-8: 1-3-5")
    print("- Sets 9-12: 1-4-5")
    print("- Odd sets start left, even sets start right")
    input("\nPress Enter to return...")

def deadlift():
    print("\n--- Deadlift ---")
    print("Goal: Build strength and resilience with moderate-to-heavy loads.")
    print("Workout:")
    print("- 3 sets of 5 reps at RPE 7/10")
    print("- Rest 2.5 minutes between sets")
    print("This should feel challenging, but you should have about 3 reps left in reserve.")
    input("\nPress Enter to return...")

def bar_core():
    print("\n--- Bar Core ---")
    print("Goal: Develop core control and stability from a hanging position.")
    print("Workout:")
    print("- Hanging Knee Raises: 3 sets of 10–15 reps")
    print("- Bent-Leg Windscreen Wipers: 3 sets of 5 reps each side (10 total)")
    print("Increase difficulty with ankle weights or slower tempo.")
    input("\nPress Enter to return...")

def bench_press():
    print("\n--- Bench Press ---")
    print("Goal: Build upper-body pushing strength.")
    print("Workout:")
    print("- 3 sets of 5 reps at RPE 7/10")
    print("- Rest 2.5 minutes between sets")
    print("Each set should be difficult but leave ~3 reps in reserve.")
    input("\nPress Enter to return...")

def weighted_pullups():
    print("\n--- Weighted Pull-ups - 85% ---")
    print("Goal: Build high-intensity pulling strength.")
    print("Workout:")
    print("- 5 sets of 3 weighted pull-ups")
    print("- Use 85% of 2RM (bodyweight + max load)")
    print("- Rest 3 minutes between sets")
    input("\nPress Enter to return...")

def on_the_minute():
    print("\n--- On the Minute Pull-ups ---")
    print("Goal: Increase volume and muscular endurance in pull pattern.")
    print("Workout:")
    print("- 5 sets of 5 pull-ups")
    print("- Rest 1 minute between sets")
    print("Progress by adding weight, reps, or reducing rest. Scale down by reducing reps or using assistance.")
    input("\nPress Enter to return...")

def one_arm_assisted():
    print("\n--- One-arm Assisted Pull-ups ---")
    print("Goal: Develop unilateral pulling strength.")
    print("Workout:")
    print("- 4 sets per arm, alternating arms")
    print("- Rest 90 seconds between sets")
    print("Use minimal assistance (bands or pulley). Adjust assistance as needed to maintain full range and proper form.")
    input("\nPress Enter to return...")

