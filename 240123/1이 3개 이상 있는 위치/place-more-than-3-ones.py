n = int(input())
arr_2d = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def how_many(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr_2d[nx][ny] == 1:
            cnt += 1
    return cnt

result = 0
for i in range(n):
    for j in range(n):
        if how_many(i, j) >= 3:
            result += 1
        
print(result)