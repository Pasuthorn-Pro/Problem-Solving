เงินกู้ = float(input("กรุณาใส่จำนวนเงินกู้: "))
if 1 <= เงินกู้ <= 1000:
    ดอกเบี้ย = เงินกู้ * 0.10
elif 1001 <= เงินกู้ <= 10000:
    ดอกเบี้ย = เงินกู้ * 0.05
else:
    ดอกเบี้ย = เงินกู้ * 0.02
ผลรวม = เงินกู้ + ดอกเบี้ย
print(f"จำนวนเงินที่ต้องชำระคืน (รวมดอกเบี้ย): {ผลรวม:.2f} บาท")