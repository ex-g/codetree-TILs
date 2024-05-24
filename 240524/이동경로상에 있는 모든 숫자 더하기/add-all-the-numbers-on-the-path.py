n, t = tuple(map(int, input().split()))
dirs = list(input())
arr = [input().split() for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
cur_dir = 0
x = y = (n-1) // 2
ans = int(arr[x][y])

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for d in dirs:
    if d == "L":
        cur_dir = (cur_dir + 3) % 4
    elif d == "R":
        cur_dir = (cur_dir + 1) % 4
    else:
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        if in_range(nx, ny):
            x, y = nx, ny
            ans += int(arr[x][y])

print(ans)