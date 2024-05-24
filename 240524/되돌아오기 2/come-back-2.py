dirs = list(input())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
ans = -1
time = 0
x, y = 0, 0
cur_dir = 2

for d in dirs:
    if d == "L":
        cur_dir = (cur_dir + 3) % 4
    elif d == "R":
        cur_dir = (cur_dir + 1) % 4
    else:
        x, y = x + dxs[cur_dir], y + dys[cur_dir]

    time += 1

    if x == 0 and y == 0:
        ans = time
        break

print(ans)