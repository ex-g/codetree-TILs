n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dxs, dys = [1, 0], [0, 1]
x, y = 0, 0
visited[x][y] = True


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

last_x, last_y = 0, 0

def dfs(x, y):
    global last_x, last_y
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and visited[nx][ny] == False and graph[nx][ny] == 1:
            visited[nx][ny] = True
            last_x, last_y = nx, ny
            dfs(nx, ny)

dfs(x, y)

if last_x == n-1 and last_y == n-1:
    print(1)
else:
    print(0)