print("***Calculate the sum between start and stop number")
start = int(input("Enter the start number: "))
stop = int(input("Enter the end number: "))
sum = 0
for i in range(start,stop +1):
    sum += i
print(f"The sum of {start} to {stop} is {sum}")