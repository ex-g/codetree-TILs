n = int(input())
arr = list(map(int, input().split()))

ans = 100

for i in range(n):
    for j in range(i + 1, n):
        if arr[j] - arr[i] < ans:
            ans = arr[j] - arr[i]

print(ans)