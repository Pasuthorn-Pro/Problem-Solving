while True:
    price = float(input("ราคาสินค้า: "))
    paid = float(input("เงินที่ลูกค้าจ่าย: "))
    
    if price <= 0:
        print("ราคาสินค้าต้องมากกว่า 0")
    elif paid < price:
        print("เงินที่จ่ายน้อยกว่าราคาสินค้า กรุณาใส่ใหม่")
    else:
        break

change = paid - price
money_type = {
    1000: "แบงค์ 1000 บาท",
    500: "แบงค์ 500 บาท",
    100: "แบงค์ 100 บาท",
    50: "แบงค์ 50 บาท",
    20: "แบงค์ 20 บาท",
    10: "เหรียญ 10 บาท",
    5: "เหรียญ 5 บาท",
    1: "เหรียญ 1 บาท"
}

print("เงินทอน:")
for value, name in money_type.items():
    count = change // value
    if count > 0:
        print(f"{name} จำนวน {int(count)} ใบ/เหรียญ")
        change %= value
