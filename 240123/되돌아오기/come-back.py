N = int(input())
x, y = 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_dict = {"E": 0, "S": 1, "W": 2, "N":3}
arr = []
cnt = 0
result = 0
judge = False
for _ in range(N):
    dir, dist = input().split()
    for _ in range(int(dist)):
        nx, ny = x + dxs[dir_dict[dir]], y + dys[dir_dict[dir]]
        x, y = nx, ny
        cnt += 1

        if x == 0 and y == 0:
            result = cnt
            judge = True

if judge:
    print(result)
else:
    print(-1)