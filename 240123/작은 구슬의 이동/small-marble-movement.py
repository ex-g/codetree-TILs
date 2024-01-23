n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)


dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
dir_dict = {"U": 0, "R": 1, "L": 2, "D": 3}
dir_num = dir_dict[d]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i in range(t):
    if in_range:
        nx, ny = r + dxs[dir_num], c + dys[dir_num]
    else: 
        dir_num = dir_dict[2 - dir_num]

print(nx + 1, ny + 1)