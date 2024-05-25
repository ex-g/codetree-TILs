n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def row_array_check(row, col_s):
    if m == 1:
        return 1
    judge = True
    for i in range(1, m):
        if grid[row][col_s] != grid[row][col_s + i]:
            judge = False
    if judge:
        return 1
    return 0


for row in range(n):
    judge = False
    for col in range(n):
        if col + m - 1 >= n:
            continue
        if row_array_check(row, col) == 1:
            judge = True
    if judge:
        ans += 1
        judge = False


def col_array_check(col, row_s):
    if m == 1:
        return 1
    judge = True
    for i in range(1, m):
        if grid[row_s][col] != grid[row_s + i][col]:
            judge = False
    if judge:
        return 1
    return 0

for col in range(n):
    judge = False
    for row in range(n):
        if row + m - 1 >= n:
            continue
        if col_array_check(col, row) == 1:
            judge = True
    if judge:
        ans += 1
        judge = False
    
print(ans)