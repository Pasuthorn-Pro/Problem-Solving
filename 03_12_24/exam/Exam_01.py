print("***Calculate sum of odd and even number (exit press 0)***")

sum_even = 0
sum_odd = 0
    
while True:
    user = (input("Enter number: "))
    num = int(user)
    if num == 0:
        break
    elif num % 2 == 0:
        sum_even += num
    elif num % 2 != 0:
        sum_odd += num

print(f"Sum of even number: {sum_even}")
print(f"Sum of odd number: {sum_odd}")