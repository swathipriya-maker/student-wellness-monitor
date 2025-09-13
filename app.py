print("📋 Student Wellness Monitor")

# Take inputs
name = input("Enter your name: ")
sleep = int(input("How many hours did you sleep last night? "))
water = int(input("How many glasses of water did you drink today? "))
stress = int(input("On a scale of 1 (low) to 10 (high), what is your stress level? "))

print("\n--- Wellness Report for", name, "---")

# Check sleep
if sleep >= 7:
    print(" Good sleep! You are well-rested.")
else:
    print("⚠ You need more rest. Aim for at least 7–8 hours.")

# Check water intake
if water >= 8:
    print(" Great! You are staying hydrated.")
else:
    print("⚠ Drink more water. 8 glasses a day is recommended.")

# Check stress
if stress <= 4:
    print(" Your stress level is under control. Keep it up!")
elif stress <= 7:
    print(" Moderate stress. Take breaks and relax.")
else:
    print(" High stress! Try meditation, exercise, or talking to a friend.")

print("\n Stay healthy and keep learning, " + name + "!")



