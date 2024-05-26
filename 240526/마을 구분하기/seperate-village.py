n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
people = 0
vilage_cnt = 0
people_cnt = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global people
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            people += 1
            visited[nx][ny] = True
            dfs(nx, ny)

for row in range(n):
    for col in range(n):
        if not visited[row][col] and grid[row][col] == 1:
            vilage_cnt += 1
            people = 1
            visited[row][col] = True
            dfs(row, col)
            people_cnt.append(people)
            people = 0

print(vilage_cnt)
people_cnt.sort()
for p in people_cnt:
    print(p)