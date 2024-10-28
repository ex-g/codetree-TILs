from collections import deque

n, h, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dist = [[-1] * n for _ in range(n)]

q = deque()
people = []
shelter = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            people.append((i, j))
        if grid[i][j] == 3:
            shelter.append((i, j))

# print("people : ", people)
# print("shleter : ", shelter)

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

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

for (i, j) in shelter:
    q.append((i, j))
    dist[i][j] = 0
    visited[i][j] = True

bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] != 2:
            print(0, end = " ")
        else:
            if not visited[i][j]:
                print(-1, end = " ")
            else:
                print(dist[i][j], end=" ")
    print()

# def initialize_visited_dist():
#     for i in range(n):
#         for j in range(n):
#             visited[i][j] = False
#             dist[i][j] = -1

# answer = [[0] * n for _ in range(n)]

# for (i, j) in people:
#     initialize_visited_dist()
#     dist[i][j] = 0
#     visited[i][j] = True
#     q.append((i, j))
#     bfs()

#     min_val = -1
#     for (k, l) in shelter:
#         if min_val == -1:
#             min_val = dist[k][l]
#         min_val = min(min_val, dist[k][l])

#     answer[i][j] = min_val

# for i in range(n):
#     for j in range(n):
#         print(answer[i][j], end=" ")
#     print()