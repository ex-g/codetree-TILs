dir_lst = list(input())
x, y = 0, 0
dx, dy = [-1, 0, 1], [0, 1, 0]

dir = 1
dir_dict = {"L": (dir + 3) % 4, "R": (dir + 1) % 4}

for elem in dir_lst:
    if elem == "F":
        x = x + dx[dir]
        y = y + dy[dir]
    else:
        dir = dir_dict[elem]

print(x, y)