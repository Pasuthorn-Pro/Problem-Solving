def calc_grade():
    # รับจำนวนวิชาจากผู้ใช้
    subj = int(input("Enter number of subjects: "))

    # ตัวแปรเก็บผลรวมเกรด
    total_grades = 0

    # ลูปเพื่อรับเกรดสำหรับแต่ละวิชา
    for i in range(1, subj + 1):
        grade = float(input(f"Enter grade for subject {i}: "))  # รับเกรดของวิชานั้น
        total_grades += grade  # เพิ่มเกรดที่ได้

    # คำนวณเกรดเฉลี่ย
    average_grade = total_grades / subj

    # แสดงผลลัพธ์
    print(f"Your average grade is: {average_grade:.2f}")


calc_grade()