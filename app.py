def get_user_input():
    print(f"--- Student Wellness Monitor for {today} ---")
    while True:
        try:
            mood_rating = int(input("How are you feeling today? (1=Bad, 5=Great): "))
            if 1 <= mood_rating <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:
            sleep_hours = float(input("How many hours did you sleep last night?: "))
            if sleep_hours >= 0:
                break
            else:
                print("Please enter a positive number for sleep.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:
            exercise_minutes = int(input("How many minutes did you exercise today?: "))
            if exercise_minutes >= 0:
                break
            else:
                print("Please enter a positive number for exercise.")
        except ValueError:
            print("Invalid input")