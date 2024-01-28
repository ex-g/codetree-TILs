n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def check(x, y):
    max_num = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and max_num < grid[nx][ny]:
            max_num = grid[nx][ny]
            max_pos = (nx, ny)

    return max_pos

def change(x, y, nx, ny):
    temp = grid[x][y]
    grid[x][y] = grid[nx][ny]
    grid[nx][ny] = temp


def turn():
    for num in range(1, n * n + 1):
        judge = False
        for row in range(n):
            for col in range(n):
                if judge == False and grid[row][col] == num:
                    judge = True
                    pos_x, pos_y = check(row, col)
                    change(row, col, pos_x, pos_y)

for _ in range(m):
    turn()

for row in range(n):
    for col in range(n):
        print(grid[row][col], end=" ")
    print()