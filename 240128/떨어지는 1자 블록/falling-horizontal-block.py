n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

point_row = 101
for row in range(0, n):
    for col in range(k - 1, k - 1 + m):
        if grid[row][col] == 1 and point_row > row:
            point_row = row
            break
            
if point_row == 101:
    point_row = 0

for col in range(k-1, k-1+m):
    grid[point_row - 1][col] = 1

for row in range(n):
    for col in range(n):
        print(grid[row][col], end=" ")
    print()