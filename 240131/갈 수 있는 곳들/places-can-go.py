from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y) or visited[x][y] != False or graph[x][y] == 1:
        return False
    return True

def bfs():
    while q:
        r, c = q.popleft()

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                visited[nr][nc] = True
                q.append((nr, nc))

q = deque()
for _ in range(k):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    q.append((r, c))
    visited[r][c] = True
    bfs()

cnt = 0
for row in range(n):
    for col in range(n):
        if visited[row][col] == True:
            cnt += 1

print(cnt)