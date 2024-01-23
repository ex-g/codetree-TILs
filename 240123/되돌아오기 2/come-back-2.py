x, y = 0, 0
dirs = list(input())
time = 0
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
dir_num = 0
dir_dict = {"L": 1}
judge = False
ans = -1

for dir in dirs:
    if dir == "L":
        time += 1
        dir_num = (dir_num + 3) % 4
    elif dir == "R":
        time += 1
        dir_num = (dir_num + 1) % 4
    elif dir == "F":
        time += 1
        x, y = x + dxs[dir_num], y + dys[dir_num]

    if x == 0 and y == 0 and judge == False:
        ans = time
        judge = True

print(ans)