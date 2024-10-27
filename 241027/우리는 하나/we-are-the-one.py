from collections import deque
n, k, u, d = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, grid_val):
    if not in_range(x, y):
        return False
    if visited[x][y] or u > abs(grid_val - grid[x][y]) or abs(grid_val - grid[x][y]) > d:
        return False

    # print("\ngrid : ", x, y, grid[x][y], grid_val)
    return True

def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def bfs():
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    q.append((i, j))
    visited[i][j] = True
    grid_val = grid[i][j]
    # print("grid_val : ", grid_val)

    while q:
        x, y = q.popleft()
        grid_val = grid[x][y]
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, grid_val):
                # print("nx, ny : ", nx, ny)
                q.append((nx, ny))
                visited[nx][ny] = True

max_val = 0
def play(i, j):
    global max_val

    initialize_visited()
    bfs()

    cnt = 0
    # print(f"{i}, {j}")
    for k in range(n):
        for l in range(n):
            if visited[k][l]:
                cnt += 1
            # print(visited[k][l], end=" ")
        # print(" ")
    # print("\n")

    max_val = max(max_val, cnt)

for i in range(n):
    for j in range(n):
        play(i, j)

print(max_val)