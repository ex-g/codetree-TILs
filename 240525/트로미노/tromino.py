# 6개를 짠다는 아이디어

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

def block1(row, col, ver):
    hap = 0
    hap += grid[row][col]
    if ver == 1:
        hap += grid[row][col + 1]
        hap += grid[row - 1][col]
    elif ver == 2:
        hap += grid[row][col + 1]
        hap += grid[row + 1][col]
    elif ver == 3:
        hap += grid[row][col - 1]
        hap += grid[row + 1][col]
    else:
        hap += grid[row][col - 1]
        hap += grid[row - 1][col]
    return hap

def block2(row, col, ver):
    hap = 0
    for i in range(3):
        if ver == 1:
            hap += grid[row][col + i]
        else:
            hap += grid[row + i][col]
    return hap

max_hap = 0

for i in range(n):
    for j in range(m):
        if j + 2 < m:
            hap = block2(i, j, 1)
            max_hap = max(max_hap, hap)

        if i + 2 < n:
            hap = block2(i, j, 2)
            max_hap = max(max_hap, hap)

        if i - 1 >= 0 and j + 1 < m:
            hap = block1(i, j, 1)
            max_hap = max(max_hap, hap)

        if i + 1 < n and j + 1 < m:
            hap = block1(i, j, 2)
            max_hap = max(max_hap, hap)

        if i + 1 < n and j - 1 >= 0:
            hap = block1(i, j, 3)
            max_hap = max(max_hap, hap)

        if i - 1 >= 0 and j - 1 >= 0:
            hap = block1(i, j, 4)
            max_hap = max(max_hap, hap)

print(max_hap)