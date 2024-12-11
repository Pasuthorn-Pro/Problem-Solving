import time
def SequencesV1(n):
    total = 0
    for i in range(n):
        total += (i + 1)
    return total

num = int(input("Input Value: "))
start = time.time()
print("ans = ", SequencesV1(num))
print("time = ", (time.time() - start) * 1000)
