n = int(input())
dp = [0] * (n+3)
dp[2] = 1
dp[3] = 1

def go_down(n, dp):
    while n > 3:
        dp[n] = (go_down(n-2, dp) + go_down(n-3, dp))

    return dp[n]

print(go_down(n, dp))