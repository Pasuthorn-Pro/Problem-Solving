# Function to get student data
def get_student_data():
    students = []
    n = int(input("Enter the number of students: "))
    for _ in range(n):
        name = input("Enter student name: ")
        score = float(input(f"Enter student score ({name}): "))
        students.append((name, score))
    return students

# Function to display the top N scores
def display_top_scores(students, top_n=3, reverse=True):
    sorted_students = sorted(students, key=lambda x: x[1], reverse=reverse)
    return sorted_students[:top_n]

# Function to search for a score
def search_score(students, target_score):
    for name, score in students:
        if score == target_score:
            return f"Found student with score {score}: {name}"
    return f"No students found with score {target_score}"

# Bubble sort implementation for scores
def bubble_sort(students):
    sorted_students = students[:]
    n = len(sorted_students)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_students[j][1] > sorted_students[j+1][1]:
                sorted_students[j], sorted_students[j+1] = sorted_students[j+1], sorted_students[j]
    return sorted_students

# Main program
if __name__ == "__main__":
    students = get_student_data()

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

    target_score = float(input("\nEnter the score to search: "))
    print(search_score(students, target_score))
