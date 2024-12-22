student_number = int(input("Enter number of students: "))

for i in range(1, student_number + 1):
    score = int(input(f"Enter score for student {i}: "))
    
    if score >= 80:
        print("Grade: A")
    elif 75 <= score <= 79:
        print("Grade: B+")
    elif 70 <= score <= 74:
        print("Grade: B")
    elif 65 <= score <= 69:
        print("Grade: C+")
    elif 60 <= score <= 64:
        print("Grade: C")
    elif 55 <= score <= 59:
        print("Grade: D+")
    elif 50 <= score <= 54:
        print("Grade: D")
    else:
        print("Grade: F")
