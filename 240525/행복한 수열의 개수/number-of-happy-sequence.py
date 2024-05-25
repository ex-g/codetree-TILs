n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
seq = [0 for _ in range(n)]

def is_happy_arr(seq):
    consecutive_cnt, max_ccnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            consecutive_cnt += 1
        else:
            consecutive_cnt = 1
        max_ccnt = max(consecutive_cnt, max_ccnt)
    return max_ccnt >= m

for i in range(n):
    seq = grid[i][:]

    if is_happy_arr(seq):
        ans += 1

for j in range(n):
    for i in range(n):
        seq[i] = grid[i][j]

    if is_happy_arr(seq):
        ans += 1

print(ans)