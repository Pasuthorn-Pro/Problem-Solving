import array as arr

number = [50, 87, 65, 39]

print(f"All array data: {list(number)}")
print(f"Maximum value: {max(number)}")
print(f"Minimum value: {min(number)}")

print(f"Sum Value: {sum(number)}")
print(f"Average: ", sum(number)/len(number))

print("Sort min to max: ", sorted(number))
print("Sort min to max: ", sorted(number,reverse=True))

odd = []
even = []

for num_odd in number:
    if num_odd % 2 != 0:
        odd.append(num_odd)

for num_even in number:
    if num_even % 2 == 0:
        even.append(num_even)

print(f"Show odd number: {list(odd)}")
print(f"Show odd number: {list(even)}")

search_num = 87
if search_num in number:
    print(f"{search_num} #พบ")
else:
    print(f"{search_num} #ไม่พบ")

search_num = 100
if search_num in number:
    print(f"{search_num} #พบ")
else:
    print(f"{search_num} #ไม่พบ")

delete_num = 65
if delete_num in number:
    number.remove(delete_num)
    print(f"{delete_num} ถูกลบแล้ว")
else:
    print(f"{delete_num} ไม่พบใน array")

print("UPdated Array", number)