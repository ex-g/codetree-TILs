n, m = tuple(map(int, input().split()))
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, d = 0, 0, 0
arr = [
    [0] * m for _ in range(n)
]

arr[x][y] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for num in range(2, n * m + 1):
    nx, ny = x + dxs[d], y + dys[d]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        d = (d + 1) % 4

    x, y = x + dxs[d], y + dys[d]
    arr[x][y] = num 

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()