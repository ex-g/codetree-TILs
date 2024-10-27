from collections import deque
n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
q = deque()
cnt = k

for _ in range(k):
    r, c = tuple(map(int, input().split()))
    r, c = r - 1, c - 1
    q.append((r, c))
    visited[r][c] = True

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def bfs():
    global cnt
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                cnt += 1 
                q.append((nx, ny))

bfs()

print(cnt)