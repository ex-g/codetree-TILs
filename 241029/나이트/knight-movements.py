from collections import deque

n = int(input())
r1, c1, r2, c2 = tuple(map(int, input().split()))
grid = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dist = [[-1] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

q = deque()
q.append((r1-1, c1-1))
visited[r1-1][c1-1] = True
dist[r1-1][c1-1] = 0
bfs()

print(dist[r2-1][c2-1])