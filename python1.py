

print("Welcome to the Daily Calories Tracker")
meals = []
calories = []

# Input section
n = int(input("Enter no. of meals you consume in a day: "))
for i in range(n):
    meal_name = input("Enter meal name: ")
    cal = float(input("Enter calories for meal: "))
    meals.append(meal_name)
    calories.append(cal)

# Calculations
total = sum(calories)
average = total / n

# Display total and average
print(f"\nTotal calories: {total:.2f}")
print(f"Average calories per meal: {average:.2f}")

# Daily calorie limit check
DAILY_LIMIT = float(input("\nEnter your daily calorie limit: "))
if total > DAILY_LIMIT:
    print("\n⚠️ You exceeded your daily limit!")
else:
    print("\n✅ You are within your daily limit!")

# --- Daily Summary ---
print("\n--- Daily Summary ---")
print(f"Total meals consumed: {n}")
print(f"Total calories: {total:.2f}")
print(f"Average calories per meal: {average:.2f}")
print(f"Daily Calorie Limit: {DAILY_LIMIT:.2f}")

if total > DAILY_LIMIT:
    print("\n⚠️ You")





