a, b = map(int, input().split())
count_arr = [0] * 9
sum_val = 0

while a > 1:
    count_arr[a % b] += 1
    a = a // b

for elem in count_arr:
    sum_val += elem ** 2
print(sum_val)