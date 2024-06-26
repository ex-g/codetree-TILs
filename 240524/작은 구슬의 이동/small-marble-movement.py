n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r) - 1, int(c) - 1
drs, dcs = [0, -1, 1, 0], [1, 0, 0, -1]
dir_dict = {
    "U" : 1,
    "D" : 2,
    "R" : 0,
    "L" : 3
}
d = dir_dict[d]

def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < n

for _ in range(t):
    nr, nc = r + drs[d], c + dcs[d]

    if in_range(nr, nc):
        r, c = nr, nc
    else:
        d = 3 - d

print(r+1, c+1)

# 26 41
# 8 3 D