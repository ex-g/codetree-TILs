n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt = [[0] * n for _ in range(n)]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    cnt[r][c] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move_bead(x, y):
    max_num = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if in_range(nx, ny) and grid[nx][ny] > max_num:
            max_pos = (nx, ny)
            max_num = grid[nx][ny]

    return max_pos

def move_all():
    cnt_next = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if cnt[row][col] == 1:
                result_1, result_2 = move_bead(row, col)
                cnt_next[result_1][result_2] = 1

    # 구슬이 2개 이상 모인 칸의 구슬 없애기
    for row in range(n):
        for col in range(n):
            if cnt_next[row][col] >= 2:
                cnt_next[row][col] = 0
    
    # cnt로 cnt_next의 값 옮겨주기
    for row in range(n):
        for col in range(n):
            cnt[row][col] = cnt_next[row][col]

for _ in range(t):
    move_all()

result = 0
for row in range(n):
    for col in range(n):
        if cnt[row][col] == 1:
            result += 1

print(result)