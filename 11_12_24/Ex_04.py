num_tri = int(input("Enter number of triangle: "))
for i in range(1, num_tri + 1):
    height = int(input(f"Enter height {i}: "))
    base = int(input(f"Enter base {i}: "))
    tri_area = 1/2 * height * base
    print(f"Triangle area {i} is {tri_area}")