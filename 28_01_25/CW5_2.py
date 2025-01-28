def get_student():
    students = []
    student_number = int(input("Enter number of students: "))
    for _ in range(student_number):
        name = input("Enter student name: ")
        score = int(input("Enter student score: "))
        students.append((name, score))
    return students

def search_student(students, target_score):
    for name, score in students:
        if score == target_score:
            return f"Found student with score {score}: {name}"
    return f"No students found with score {target_score}"

def get_score(student):
    return student[1]

def display_top_scores(students, top_n=3, reverse=True):
    sorted_students = sorted(students, key=get_score, reverse=reverse)
    return sorted_students[:top_n]

def bubble_sort(students):
    sorted_students = students[:]
    n = len(sorted_students)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_students[j][1] > sorted_students[j + 1][1]:
                sorted_students[j], sorted_students[j + 1] = sorted_students[j + 1], sorted_students[j]
    return sorted_students

if __name__ == "__main__":
    students = get_student()

    print("\n--Unsorted Scores--")
    for name, score in students:
        print(f"{name}: {score}")

    print("\n--Top 3 Highest Scores--")
    for name, score in display_top_scores(students, top_n=3, reverse=True):
        print(f"{name}: {score}")

    print("\n--Top 3 Lowest Scores--")
    for name, score in display_top_scores(students, top_n=3, reverse=False):
        print(f"{name}: {score}")

    print("\n--Sorted Scores (Bubble Sort)--")
    sorted_students = bubble_sort(students)
    for name, score in sorted_students:
        print(f"{name}: {score}")

    target_score = int(input("\nEnter the score to search: "))
    print(search_student(students, target_score))
