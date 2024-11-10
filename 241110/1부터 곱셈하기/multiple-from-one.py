n = int(input())
mul_val = 1

for i in range(1, 11):
    mul_val *= i
    if mul_val >= n:
        print(i)
        break