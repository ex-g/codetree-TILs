n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
bomb_num = 0
max_num = 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False 
    if visited[x][y] or grid[x][y] != block_num:
        return False
    return True

def dfs(x, y):
    global block_cnt
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            block_cnt += 1
            visited[nx][ny] = True
            dfs(nx, ny)

for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            block_num = grid[row][col]
            block_cnt = 1
            visited[row][col] = True
            dfs(row, col)
            if block_cnt >= 4:
                bomb_num += 1
            if max_num < block_cnt:
                max_num = block_cnt

print(bomb_num, max_num)