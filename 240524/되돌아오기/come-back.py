n = int(input())
x, y = 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
ans = -1
time = 0
mapper = {
    "E" : 0,
    "S" : 1,
    "W" : 2,
    "N" : 3
}

def move(d, dist):
    global x, y, ans, time 

    for _ in range(dist):
        x, y = x + dxs[d], y + dys[d]
        time += 1
        if x == 0 and y == 0:
            ans = time
            return True
    return False


for _ in range(n):
    d, dist = tuple(input().split())
    d, dist = mapper[d], int(dist)

    done = move(d, dist)

    if done:
        break

print(ans)