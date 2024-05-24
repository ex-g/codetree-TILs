# 처음 위치랑 같아지면 초를 출력해라

n = int(input())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
mapper = {
    "E" : 0,
    "S" : 1,
    "W" : 2,
    "N" : 3
}
time = 0
x, y = 0, 0
arr = []

for _ in range(n):
    d, dist = input().split()
    d, dist = mapper[d], int(dist)
    arr.append((d, dist))

for d, dist in arr:
    for _ in range(dist):
        x, y = x + dxs[d], y + dys[d]
        time += 1
        if x == 0 and y == 0:
            print(time)
            break

if time == 0:
    print(-1)