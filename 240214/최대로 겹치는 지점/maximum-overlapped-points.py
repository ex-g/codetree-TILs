n = int(input())
arr = [0] * 101

for i in range(n):
    x1, x2 = map(int, input().split())
    for j in range(x1, x2+1):
        arr[j] += 1

max_val = 0
for i in arr:
    if i > max_val:
        max_val = i

print(max_val)