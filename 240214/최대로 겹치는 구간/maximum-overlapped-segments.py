n = int(input())
arr = [0] * 200

for i in range(n):
    x1, x2 = map(int, input().split())
    x1, x2 = x1 + 100, x2 + 100
    for j in range(x1, x2):
        arr[j] += 1

max_val = 0
for i in arr:
    if i > max_val:
        max_val = i
print(max_val)