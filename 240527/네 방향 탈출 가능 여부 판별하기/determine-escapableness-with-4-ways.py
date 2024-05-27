from collections import deque

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()
q.append((0, 0))
visited[0][0] = True

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def bfs():
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
        
bfs()

# for row in range(n):
#     for col in range(m):
#         print(visited[row][col], end=" ")
#     print()

if visited[n-1][m-1]:
    print(1)
else:
    print(0)