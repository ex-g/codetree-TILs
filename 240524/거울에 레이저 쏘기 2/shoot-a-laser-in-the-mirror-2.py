n = int(input())
arr = [list(input()) for _ in range(n)]
razer = int(input())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

# 처음 들어오게 되는 위치별 방향 : 1~3 : D, 4~6 : L, 7~9 : U, 10~12 : R
# 처음 x, y 좌표
if razer < n:
    cur_dir = 0
    x, y = 0, razer - 1
elif razer < 2 * n:
    cur_dir = 1
    x, y = (razer % n) - 1, n - 1
elif razer < 3 * n:
    cur_dir = 2
    x, y = n - 1, 3 * n - razer
else:
    cur_dir = 3
    x, y = 4 * n - razer, 0

def change_dir(cur_dir, x, y):
    if arr[x][y] == "\\":
        cur_dir = 3 - cur_dir
    else:
        cur_dir = cur_dir ^ 1
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

# xor 비트 연산 사용
# 00 ^ 01 = 01
# 01 ^ 01 = 00
# 10 ^ 01 = 11
# 11 ^ 01 = 10