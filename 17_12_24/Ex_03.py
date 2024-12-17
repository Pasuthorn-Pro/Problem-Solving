first = int(input("Enter first number: "))
last = int(input("Enter the last number: "))
for number in range(first, last + 1):
    if number % 3 == 0:
        print(number)