arr = list(map(int, input().split()))
judge = False
total = 0
average = 0

for i in range(len(arr)):
    if arr[i] >= 250:
        break
    total += arr[i]
    average = total / (i+1)

print(total, round(average, 1))