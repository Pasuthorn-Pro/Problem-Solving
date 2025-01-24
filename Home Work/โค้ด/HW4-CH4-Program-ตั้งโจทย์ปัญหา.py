students = []

def add_student():
    print("\n--- เพิ่มข้อมูลนักเรียน ---")
    student_id = input("กรอกรหัสนักเรียน: ")
    
    # ตรวจสอบรหัสนักเรียนไม่ให้ซ้ำ
    for student in students:
        if student["student_id"] == student_id:
            print("รหัสนักเรียนนี้มีอยู่แล้ว!")
            return
    
    name = input("กรอกชื่อนักเรียน: ")
    try:
        scores = [
            float(input("กรอกคะแนนวิชา 1 (0-100): ")),
            float(input("กรอกคะแนนวิชา 2 (0-100): ")),
            float(input("กรอกคะแนนวิชา 3 (0-100): "))
        ]
        if any(score < 0 or score > 100 for score in scores):
            print("คะแนนต้องอยู่ระหว่าง 0-100!")
            return
    except ValueError:
        print("กรุณากรอกคะแนนเป็นตัวเลข!")
        return
    
    # เพิ่มนักเรียนในโครงสร้างข้อมูล
    students.append({
        "student_id": student_id,
        "name": name,
        "score": scores
    })
    print("เพิ่มข้อมูลนักเรียนเรียบร้อย!")

def show_students():
    print("\n--- แสดงข้อมูลนักเรียนทั้งหมด ---")
    if not students:
        print("ไม่มีข้อมูลนักเรียนในระบบ")
        return
    
    for student in students:
        print(f"รหัส: {student['student_id']}, ชื่อ: {student['name']}, คะแนน: {student['score']}")

def find_student():
    print("\n--- ค้นหานักเรียน ---")
    student_id = input("กรอกรหัสนักเรียนที่ต้องการค้นหา: ")
    for student in students:
        if student["student_id"] == student_id:
            print(f"รหัส: {student['student_id']}, ชื่อ: {student['name']}, คะแนน: {student['score']}")
            return
    print("ไม่พบข้อมูลนักเรียนในระบบ!")

def calculate_average():
    print("\n--- คำนวณคะแนนเฉลี่ย ---")
    if not students:
        print("ไม่มีข้อมูลนักเรียนในระบบ")
        return
    
    for student in students:
        average = sum(student["score"]) / len(student["score"])
        print(f"รหัส: {student['student_id']}, ชื่อ: {student['name']}, คะแนนเฉลี่ย: {average:.2f}")

def main():
    while True:
        print("\n--- ระบบจัดการข้อมูลนักเรียน ---")
        print("1. เพิ่มข้อมูลนักเรียน")
        print("2. แสดงรายชื่อนักเรียนทั้งหมด")
        print("3. ค้นหานักเรียนจากรหัส")
        print("4. คำนวณคะแนนเฉลี่ยของนักเรียนแต่ละคน")
        print("5. ออกจากโปรแกรม")
        
        choice = input("เลือกเมนู: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            find_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            print("ออกจากโปรแกรม")
            break
        else:
            print("กรุณาเลือกเมนูที่ถูกต้อง!")

# เริ่มโปรแกรม
main()