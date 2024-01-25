n, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2)]

def change(grid, n):
    up_temp = grid[0][n - 1]
    down_temp = grid[1][n -1]

    for i in range(n-1, 0, -1):
        grid[0][i] = grid[0][i - 1]
        grid[1][i] = grid[1][i - 1]

    grid[0][0] = down_temp
    grid[1][0] = up_temp


    return grid

for _ in range(t):
    grid = change(grid, n)

for row in range(2):
    for col in range(n):
        print(grid[row][col], end=" ")
    print()