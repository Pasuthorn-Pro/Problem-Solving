print("***Convert BMI")
W = float(input("Enter your weight(kg): "))
H = float(input("Enter your height(m): "))
BMI = W/(H**2)
#print(f"Your BMI is {BMI:.5f}")
print("Your BMI is ",(BMI, ".5f"))