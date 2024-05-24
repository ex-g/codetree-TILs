n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
drs, dcs = [1, 0, 0, -1], [0, -1, 1, 0]
dir_dict = {
    "U" : 2,
    "D" : 1,
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

print(r+1, c+1)