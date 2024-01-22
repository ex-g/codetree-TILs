arr = list(map(int, input().split()))
total_sum = 0
cnt = 0

for elem in arr:
    if elem == 0:
        break
    elif elem % 2 == 0:
        total_sum += elem
        cnt += 1

print(cnt, total_sum)