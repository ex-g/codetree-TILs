n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input().split()))

def get_cnt(row_s, row_e, col_s, col_e):
    cnt = 0
    for i in range(row_s, row_e + 1):
        for j in range(col_s, col_e + 1):
            if grid[i][j] == "1":
                cnt += 1
    return cnt 

max_cnt = 0

for row in range(n):
    for col in range(n):
        if row + 2 >= n or col + 2 >= n:
            continue

        cnt = get_cnt(row, row + 2, col, col + 2)

        max_cnt = max(max_cnt, cnt)

print(max_cnt)