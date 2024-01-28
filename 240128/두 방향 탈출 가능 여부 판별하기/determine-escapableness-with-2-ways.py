n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = [[0] * m for _ in range(n)]
order = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or graph[x][y] == 0:
        return False

    return True

def dfs(x, y):
    global order 

    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            answer[nx][ny] = order
            order += 1
            visited[nx][ny] = 1
            dfs(nx, ny)

answer[0][0] = order
order += 1
visited[0][0] = 1
dfs(0, 0)

if answer[n-1][m-1] != 0:
    print(1)
else:
    print(0)