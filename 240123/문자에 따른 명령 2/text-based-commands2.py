dir_lst = list(input())
x, y = 0, 0
dir_num = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


for elem in dir_lst:
    dir_dict = {"L": (dir_num + 3) % 4, "R": (dir_num + 1) % 4}
    if elem == "F":
        x = x + dx[dir_num]
        y = y + dy[dir_num]
    else:
        dir_num = dir_dict[elem]

print(x, y)