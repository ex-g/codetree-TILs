n, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(3)]


def change():
    temp1 = grid[0][n-1]
    temp2 = grid[1][n-1]
    temp3 = grid[2][n-1]

    for i in range(n):
        for j in range(n-2, -1, -1):
            grid[i][j + 1] = grid[i][j]

    grid[0][0] = temp3
    grid[1][0] = temp1
    grid[2][0] = temp2

for _ in range(t):
    change()

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()