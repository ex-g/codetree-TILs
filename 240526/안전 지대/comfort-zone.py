n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
max_safe = 0
max_safe_k = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# can_go
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or safe_grid[x][y] == 0:
        return False
    return True

# dfs
def dfs(x, y):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy 
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)

# max_k 구하기
max_k = 0
for row in range(n):
    for col in range(m):
        max_k = max(max_k, grid[row][col])

# print("max_k :", max_k)


# k를 1부터 max_k까지 돌리기
for k in range(1, max_k + 1):
    visited = [[False] * m for _ in range(n)]
    safe_cnt = 0
    
    # safe grid 만들기
    safe_grid = [[0] * m for _ in range(n)] # 안전하면 1, 잠기면 0
    # print(safe_grid)

    for row in range(n):
        for col in range(m):
            if grid[row][col] > k:
                safe_grid[row][col] = 1

    # print(f"k가 {k}일 때 safe_grid")
    # for r in range(n):
    #     for c in range(m):
    #         print(safe_grid[r][c], end=" ")
    #     print()


    for row in range(n):
        for col in range(m):
            if not visited[row][col] and safe_grid[row][col] == 1:
                safe_cnt += 1
                visited[row][col] = True
                dfs(row, col)
            if safe_cnt > max_safe:
                max_safe = safe_cnt
                max_safe_k = k

print(max_safe_k, max_safe)