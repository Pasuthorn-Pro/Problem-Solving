while True:
    first = int(input("Enter first number: "))
    last = int(input("Enter the last number: "))
    divisor = int(input("Enter divisor: "))
    for number in range(first + 1, last):
        if number % divisor == 0:
            print(number)

    continue_program = int(input("Do you want to continue program (1 for Yes / 0 for No ): "))
    if continue_program == 0:
        break