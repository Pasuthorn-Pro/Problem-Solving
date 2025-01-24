# Python program to demonstrate
# Adding Elements to an Array
# importing "array" for array creations
import array as arr

# array with int type
a = arr.array('i', [1, 2, 3])

# Array before insertion
print("Array before insertion: ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

# Inserting an element using insert() function
a.insert(1, 4)

# Array after insertion
print("\nArray after insertion: ", end=" ")
for i in a:
    print(i, end=" ")
print()  # To add a newline after printing the array

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# Array before insertion
print("Array before insertion: ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()

# Adding an element using append()
b.append(4.4)

# Array after insertion
print("Array after insertion: ", end=" ")
for i in b:
    print(i, end=" ")
print()  # To add a newline after printing the array

a.append(5)
print(a)
a.remove(2)
print(a)