n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_happy_arr(row, col):
    cnt = 0
    judge = True
    for i in range(1, m):
        if grid[row][col] != grid[row][col+i]:
            judge = False
    if judge:
        cnt += 1

    return cnt

ans = 0

for row in range(n):
    for col in range(n):
        if col + m > n:
            continue
        ans += get_happy_arr(row, col)
        
for col in range(n):
    for row in range(n):
        if row + m > n:
            continue
        ans += get_happy_arr(col, row)

print(ans)