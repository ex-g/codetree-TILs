arr = list(map(int, input().split()))
cnt = 0
total = 0
average = 0

for elem in arr:
    if elem == 0:
        break
    cnt += 1


for elem in arr[:cnt]:
    total += elem

print(f'{total} {total / cnt:.1f}')