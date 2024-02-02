import sys
min_val = sys.maxsize

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][n-1] = grid[0][n-1]

def initialize():
    for i in range(n-2, -1, -1):
        dp[0][i] = grid[0][i] + dp[0][i+1]

    for i in range(1, n):
        dp[i][n-1] = grid[i][n-1] + dp[i-1][n-1]

initialize()

for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i][j+1], dp[i-1][j]) + grid[i][j]

ans = min_val
for i in range(n):
    ans = min(ans, dp[n-1][i])

print(ans)