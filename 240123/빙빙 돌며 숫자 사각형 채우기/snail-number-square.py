n, m = tuple(map(int, input().split()))
answer = [[0] * m for _ in range(n)]
x, y = 0, 0
answer[x][y] = 1
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i

for i in range(n):
    for j in range(m):
        print(answer[i][j], end= " ")
    print()