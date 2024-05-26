n, m = tuple(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
cnt = 0

for _ in range(m):
    a, b = tuple(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False for _ in range(n + 1)]

def dfs(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True 
            dfs(curr_v)
    return cnt
        
visited[1] = True
print(dfs(1))