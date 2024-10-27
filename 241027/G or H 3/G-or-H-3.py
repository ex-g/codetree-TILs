N, K = tuple(map(int, input().split()))
placed = [0] * 10001

for _ in range(N):
    where, alpha = input().split()
    where = int(where)
    if alpha == "G":
        placed[where] = 1
    else:
        placed[where] = 2

max_cnt = 0
for i in range(1, 10000 - K + 1):
    sum_val = 0
    for j in range(i, i + K + 1):
        sum_val += placed[j]
    max_cnt = max(max_cnt, sum_val)

print(max_cnt)