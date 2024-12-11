distance = int(input("กรุณาระบุระยะทาง (กิโลเมตร): "))
transport_mode = input("เลือกพาหนะ (รถยนต์/รถไฟฟ้า): ")

if transport_mode == "1":
    cost = distance * 4
elif transport_mode == "2":
    cost = distance * 1

print(f"ค่าใช้จ่ายในการเดินทางด้วย {transport_mode} ระยะทาง {distance} กิโลเมตร คือ {cost} บาท")
