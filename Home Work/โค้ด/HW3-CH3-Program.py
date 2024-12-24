#Big O(1)
import time

def calculate_sums_optimized(N):
    # คำนวณผลรวมของเลขทั้งหมด
    total_sum = N * (N + 1) // 2
    
    # คำนวณผลรวมของเลขคู่
    last_even = N if N % 2 == 0 else N - 1  # เลขคู่สุดท้าย
    number_of_evens = last_even // 2  # จำนวนเลขคู่
    sum_even = number_of_evens * (2 + last_even) // 2  # ผลรวมของเลขคู่
    
    # คำนวณผลรวมของเลขคี่
    sum_odd = total_sum - sum_even
    
    return sum_odd, sum_even

# รับค่า N จากผู้ใช้
N = int(input("Enter the value of N: "))

# เริ่มการวัดเวลา
start_time = time.time()

# คำนวณผลรวม
sum_odd, sum_even = calculate_sums_optimized(N)

# หยุดการวัดเวลา
end_time = time.time()

# แสดงผลลัพธ์
print(f"Sum of odd numbers: {sum_odd}")
print(f"Sum of even numbers: {sum_even}")
print(f"Execution time: {(end_time - start_time) * 1000:.3f} ms")
