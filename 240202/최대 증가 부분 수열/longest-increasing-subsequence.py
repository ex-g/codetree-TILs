import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

def init():
    for i in range(n):
        dp[i] = INT_MIN

    dp[0] = 1

init()

for i in range(1, n):
    for j in range(0, i):
        if dp[j] == INT_MIN:
            continue
        
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

ans = -sys.maxsize
for i in range(n):
    ans = max(ans, dp[i])

print(ans)