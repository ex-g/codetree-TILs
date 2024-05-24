n, m = tuple(map(int, input().split()))
x, y = 0, 0
init_num = 66
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cur_dir = 0
arr = [[0] * m for _ in range(n)]
arr[x][y] = "A"

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for num in range(2, n * m + 1):
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        cur_dir = (cur_dir + 1) % 4

    x, y = x + dxs[cur_dir], y + dys[cur_dir]
    arr[x][y] = chr(init_num)
    if init_num == 90:
        init_num = 65
    else:
        init_num += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()