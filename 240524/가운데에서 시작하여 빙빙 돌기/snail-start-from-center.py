n = int(input())
x, y = (n-1)//2, (n-1)//2
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
arr = [[0] * n for _ in range(n)]
arr[x][y] = 1
cur_dir = 3

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for num in range(2, n * n + 1):
    cur_dir = (cur_dir + 1) % 4
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        cur_dir = (cur_dir + 3) % 4

    x, y = x + dxs[cur_dir], y + dys[cur_dir]
    arr[x][y] = num

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()