n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
arr = []
max_bomb = 0

cnt = 0
bomb_lst = []
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            bomb_lst.append((row, col))
            cnt += 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bomb_first(temp, x, y):
    dxs, dys = [-1, -2, 1, 2], [0, 0, 0, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny):
            temp[nx][ny] += 1

def bomb_second(temp, x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny):
            temp[nx][ny] += 1

def bomb_third(temp, x, y):
    dxs, dys = [-1,-1, 1, 1], [-1, 1, -1, 1]
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny):
            temp[nx][ny] += 1
    
def bomb(arr):
    result = 0
    temp = [[0] * n for _ in range(n)]
    for bomb in bomb_lst:
        temp[bomb[0]][bomb[1]] = 1

    for grid_cnt, bomb_type in zip(bomb_lst, arr):
        if bomb_type == 1:
            bomb_first(temp, grid_cnt[0], grid_cnt[1])
        elif bomb_type == 2:
            bomb_second(temp, grid_cnt[0], grid_cnt[1])
        elif bomb_type == 3:
            bomb_third(temp, grid_cnt[0], grid_cnt[1])


    for row in range(n):
        for col in range(n):
            if temp[row][col] >= 1:
                result += 1
    return result


def choose(curr_num):
    global max_bomb
    if curr_num == cnt + 1:
        result = bomb(arr)
        if max_bomb < result:
            max_bomb = result
        return

    for i in range(1, 4):
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

choose(1)
print(max_bomb)