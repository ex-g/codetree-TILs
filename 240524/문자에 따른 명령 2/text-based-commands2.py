x, y = 0, 0
str = list(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3

for e in str:
    if e == "L":
        dir_num = (dir_num + 3) % 4
    elif e == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)