n = int(input())
arr = [0] * 2001
current_x = 1000

for i in range(n):
    x, D = input().split()
    x = int(x)

    if D == "R":
        for j in range(current_x, current_x + x):
            arr[j] += 1
        current_x += x
    else:
        for j in range(current_x - x, current_x):
            arr[j] += 1
        current_x -= x

result = 0
for i in arr:
    if i >= 2:
        result += 1

print(result)