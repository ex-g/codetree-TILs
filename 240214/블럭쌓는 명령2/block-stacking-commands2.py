n, k = map(int, input().split())
arr = [0] * (n + 1)

for i in range(k):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        arr[j] += 1

max_val = 0
for i in arr:
    if max_val < i:
        max_val = i
print(max_val)