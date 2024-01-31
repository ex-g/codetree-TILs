from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _  in range(n)]
visited = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range or visited[x][y] or graph[x][y] == 0:
        return False
    return True

def bfs():
    while q:
        r, c = q.popleft()

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                visited[nr][nc] = 1
                q.append((nr, nc))

q = deque()
q.append((0, 0))
bfs()

print(visited[n-1][m-1])