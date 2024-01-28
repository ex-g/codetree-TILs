n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1
origin_r, origin_c = r, c
bomb_num = grid[r][c] - 1
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 폭탄 터지기
grid[r][c] = 0
for dx, dy in zip(dxs, dys):
    r, c = origin_r, origin_c
    for _ in range(bomb_num):
        nr, nc = r + dx, c + dy
        if in_range(nr, nc):
            grid[nr][nc] = 0
            r, c = nr, nc

# temp 생성
temp = [[0] * n for _ in range(n)]

# temp에 정리된 거 복제
for col in range(n):
    temp_row = n - 1
    for row in range(n-1, -1, -1):
        if grid[row][col] != 0:
            temp[temp_row][col] = grid[row][col]
            temp_row -= 1

# temp 출력
for i in range(n):
    for j in range(n):
        print(temp[i][j], end=" ")
    print()