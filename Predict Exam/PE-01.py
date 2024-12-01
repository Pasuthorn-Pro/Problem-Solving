print("***Find prime number in a given range***")
start = int(input("Enter the start of the range: "))
stop = int(input("Enter the stop of the range: "))

for num in range(start, stop + 1):  # วนซ้ำในช่วง start ถึง stop
    if num > 1:  # ตรวจสอบว่า num มากกว่า 1
        is_prime = True  # กำหนดสถานะเป็นจำนวนเฉพาะเบื้องต้น
        for i in range(2, num):  # วนซ้ำเพื่อตรวจสอบตัวหาร
            if num % i == 0:  # ถ้า num ถูกหารลงตัว
                is_prime = False  # ไม่ใช่จำนวนเฉพาะ
                break  # หยุดการตรวจสอบ
        if is_prime:  # ถ้าเป็นจำนวนเฉพาะ
            print(num)  # แสดงผล