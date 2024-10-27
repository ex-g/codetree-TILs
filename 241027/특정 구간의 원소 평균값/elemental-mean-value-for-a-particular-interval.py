N = int(input())
arr = list(tuple(map(int, input().split())))
cnt = 0

for i in range(N):
    for j in range(i, N):
        average = 0
        for k in range(i, j + 1):
            average += arr[k]
        average //= j - i + 1
        if any(arr) == average:
            cnt += 1

print(cnt)