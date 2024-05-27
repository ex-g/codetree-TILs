from collections import deque

n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque()
for _ in range(k):
    x, y = tuple(map(int, input().split()))
    x, y = x - 1, y - 1
    visited[x][y] = True
    q.append((x, y))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

bfs()

# print(visited)
cnt = 0
for row in range(n):
    for col in range(n):
        if visited[row][col]:
            cnt += 1

print(cnt)