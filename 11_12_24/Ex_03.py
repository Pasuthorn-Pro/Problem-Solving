def calculate_salary(hours_worked, hourly_rate):
    if hours_worked <= 160:
        salary = hours_worked * hourly_rate
    else:
        salary = (160 * hourly_rate) + ((hours_worked - 160) * hourly_rate * 1.5)
    return salary


hours_worked = float(input("กรุณากรอกจำนวนชั่วโมงทำงาน: "))
hourly_rate = float(input("กรุณากรอกอัตราค่าแรงต่อชั่วโมง: "))

salary = calculate_salary(hours_worked, hourly_rate)
print(f"เงินเดือนที่ได้รับ: {salary} บาท")
