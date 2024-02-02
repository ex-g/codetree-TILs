n = int(input())
dp = [0] * (n+3)
dp[2] = 1
dp[3] = 1

def go_down(n, dp):
    if n == 1:
        return 0
    if n == 2:
        return 1
    elif n == 3:
        return 1
    else:
        if dp[n]:
            return dp[n]
        else:
            dp[n] = (go_down(n-2, dp) + go_down(n-3, dp))

    return dp[n]

print(go_down(n, dp) % 10007)