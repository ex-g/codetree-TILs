n, r, c= map(int, input().split())
r, c = r-1, c-1
grid = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def simulate():
    global r, c
    max_num = grid[r][c]
    judge = False

    for dx, dy in zip(dxs, dys):
        nr, nc = r + dx, c + dy

        if in_range(nr, nc) and max_num < grid[nr][nc]:
            max_num = grid[nr][nc]
            print(max_num, end = " ")
            r, c = nr, nc
            judge = True
            return judge

print(grid[r][c], end= " ")

for _ in range(n * n):
    simulate()