hour = int(input("Enter work hour: "))
work_rate = int(input("Enter work rate: "))
if hour <= 160:
    salary = hour * work_rate
    print(f"Salary is {salary}")
else:
    salary = (160 * work_rate) + ((hour - 160) * (work_rate * 1.5))
    print(f"Salary is {salary}")