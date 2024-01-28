n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

cnt = 1
def dfs(root_vertex):
    global cnt
    for curr_v in graph[root_vertex]:
        if visited[curr_v] == False:
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)


root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)
print(cnt)