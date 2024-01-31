n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt_lst = []
cnt = 0
vil = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y) or visited[x][y] == True or graph[x][y] != 1:
        return False
    return True


def dfs(x, y):
    global cnt

    cnt += 1
    visited[x][y] = True

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            dfs(nx, ny)
    
    
for row in range(n):
    for col in range(n):
        if graph[row][col] == 1 and visited[row][col] == False:
            vil += 1
            dfs(row, col)
        if cnt != 0:
            cnt_lst.append(cnt)
            cnt = 0


print(vil)

cnt_lst = sorted(cnt_lst)

for elem in cnt_lst:
    print(elem)