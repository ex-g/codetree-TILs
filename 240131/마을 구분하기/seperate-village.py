n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt_lst = []
cnt = 0
vil = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y):
    global cnt

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and graph[nx][ny] == 1:
            cnt += 1
            graph[nx][ny] = 0
            dfs(nx, ny)
    
    if cnt != 0:
        cnt_lst.append(cnt)
    cnt = 0

for row in range(n):
    for col in range(n):
        if graph[row][col] == 1:
            graph[row][col] = 0
            cnt += 1
            vil += 1
            dfs(row, col)


print(vil)

cnt_lst = sorted(cnt_lst)

for elem in cnt_lst:
    print(elem)