stored_calorie = []

def run_calorie():
    time = int(input("Enter running time(minutes): "))
    calorie_burned = time * 10
    stored_calorie.append(calorie_burned)
    print(f"Calories burned from running: {calorie_burned:.2f}")

def cycling_calorie():
    time = int(input("Enter cycling time(minutes): "))
    calorie_burned = time * 8
    stored_calorie.append(calorie_burned)
    print(f"Calories burned from cycling: {calorie_burned:.2f}")

def swim_calorie():
    time = int(input("Enter swimming time(minutes): "))
    calorie_burned = time * 5
    stored_calorie.append(calorie_burned)
    print(f"Calories burned from swimming: {calorie_burned:.2f}")

def show_stored_calorie():
    total_calories = sum(stored_calorie)
    print(f"Total calories burned: {total_calories:.2f} kcal")

def main():
    while True:
        print("\n--- Choose Menu ---")
        print("1. Calculate running calorie")
        print("2. Calculate cycling calorie")
        print("3. Calculate swimming calorie")
        print("4. Show stored calorie")
        print("5. Stop program \n")

        choice = input("Choose menu: ")
        if choice == "1":
            run_calorie()
        elif choice == "2":
            cycling_calorie()
        elif choice == "3":
            swim_calorie()
        elif choice == "4":
            show_stored_calorie()
        elif choice == "5":
            print("Stop program")
            break

main()
