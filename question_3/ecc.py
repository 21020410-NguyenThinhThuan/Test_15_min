# 
# tìm a, b sao cho Tổng số điểm đường cong (E) là số nguyên tố. Với p là số nguyên tố 
#

from sympy import isprime
import random

def generate_prime(bits):
    while True:
        p = random.randint(2**(bits-1), 2**bits - 1)
        if isprime(p):
            return p

def find_prime_points(p):
    while True:
        a = random.randint(1, p-1)
        b = random.randint(1, p-1)
        points_count = 1  # Điểm vô cùng

        for x in range(p):
            x_3 = pow(x, 3, p)
            for y in range(p):
                y_2 = pow(y, 2, p)
                if (y_2 - x_3 - a*x - b) % p == 0:
                    points_count += 1

        # Kiểm tra points_count có phải là số nguyên tố
        if isprime(points_count):
            return a, b, points_count


# Tìm a và b
p = 2531
a, b, points_count = find_prime_points(p)

print(f"Tìm thấy a và b thoả mãn điều kiện:")
print(f"a = {a}")
print(f"b = {b}")
print(f"Tổng số điểm trên đường cong là số nguyên tố: {points_count}")
print(f"p = {p}")