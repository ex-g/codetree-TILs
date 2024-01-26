n, r, c= map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = r-1, c-1
print(grid[r][c], end= " ")
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


for dx, dy in zip(dxs, dys):
    nr, nc = r + dx, c + dy
    if in_range(nr, nc) and grid[r][c] < grid[nr][nc]:
        print(grid[nr][nc], end=" ")
        r, c = nr, nc