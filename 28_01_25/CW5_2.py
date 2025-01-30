def get_student():
    students = []
    student_number = int(input("Enter number of students: "))
    for _ in range(student_number):
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))  # เปลี่ยนเป็น float เพื่อรองรับทศนิยม
        students.append((name, score))
    return students

def search_student(students, target_score):
    matched_students = [name for name, score in students if score == target_score]
    if matched_students:
        return f"Found {len(matched_students)} student(s) with score {target_score}: {', '.join(matched_students)}"
    return f"No students found with score {target_score}"

def get_score(student):
    return student[1]

def display_top_scores(students, top_n=3, reverse=True):
    sorted_students = sorted(students, key=get_score, reverse=reverse)
    return sorted_students[:top_n]

def bubble_sort(students):
    sorted_students = students[:]  # ทำสำเนารายชื่อ เพื่อไม่ให้กระทบข้อมูลต้นฉบับ
    n = len(sorted_students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_students[j][1] > sorted_students[j + 1][1]:
                sorted_students[j], sorted_students[j + 1] = sorted_students[j + 1], sorted_students[j]
    return sorted_students

if __name__ == "__main__":
    students = get_student()

    print("\n-- Unsorted Scores --")
    for name, score in students:
        print(f"{name}: {score}")
    print("\n-- Sorted Scores (Bubble Sort) --")
    sorted_students = bubble_sort(students)
    
    for name, score in sorted_students:
        print(f"{name}: {score}")
    print("\n-- Top 3 Highest Scores --")
    top_highest = display_top_scores(sorted_students, top_n=3, reverse=True)
    
    for name, score in top_highest:
        print(f"{name}: {score}")
    print("\n-- Top 3 Lowest Scores --")
    top_lowest = display_top_scores(sorted_students, top_n=3, reverse=False)
    
    for name, score in top_lowest:
        print(f"{name}: {score}")
    target_score = float(input("\nEnter the score to search: "))
    print(search_student(students, target_score))
