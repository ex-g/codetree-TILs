n = int(input())
arr = [list(input()) for _ in range(n)]
razer = int(input())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

# 처음 들어오게 되는 위치별 방향 : 1~3 : D, 4~6 : L, 7~9 : U, 10~12 : R
# 처음 x, y 좌표
if 0 <= razer < n:
    cur_dir = 0
    x, y = 0, razer - 1
elif n <= razer < 2 * n:
    cur_dir = 1
    x, y = (razer % n) - 1, n - 1
elif 2 * n <= razer < 3 * n:
    cur_dir = 2
    x, y = n - 1, 3 * n - razer
else:
    cur_dir = 3
    x, y = 4 * n - razer, 0

def change_dir(cur_dir, x, y):
    if cur_dir == 0:
        if arr[x][y] == "/":
            cur_dir = 1
        else:
            cur_dir = 3
    elif cur_dir == 1:
        if arr[x][y] == "/":
            cur_dir = 0
        else:
            cur_dir = 2
    elif cur_dir == 2:
        if arr[x][y] == "/":
            cur_dir = 3
        else:
            cur_dir = 1
    else:
        if arr[x][y] == "/":
            cur_dir = 2
        else:
            cur_dir = 0
    return cur_dir

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

cnt = 1
while True:
    # print(f"현재 방향은 {cur_dir}입니다. 위치는 {x}, {y}")
    cur_dir = change_dir(cur_dir, x, y)
    # print(f"바뀐 방향은 {cur_dir}입니다.")

    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]

    if not in_range(nx, ny):
        break

    x, y = x + dxs[cur_dir], y + dys[cur_dir]
    cnt += 1
    # print(f"레이저가 튕겼습니다. 현재 갯수 : {cnt}, 위치는 {x}, {y}")
    # print()
    
print(cnt)