n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(1, m + 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for i in range(n + 1)]
visited[1] = True

def dfs(vertex):
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)

dfs(1)

cnt = 0
for i in visited:
    if i: cnt += 1
print(cnt-1)