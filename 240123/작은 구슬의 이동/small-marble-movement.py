n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
dir_dict = {"R": 0, "D": 1, "U": 2, "L": 3}
dir_num = dir_dict[d]

def in_range(x, y):
    return 1 <= x < n+1 and 1 <= y < n+1

for i in range(t):
    nx, ny = r + dxs[dir_num], c + dys[dir_num]
    if in_range(nx, ny):
        r, c = nx, ny
    else: 
        dir_num = 3 - dir_num

print(r, c)