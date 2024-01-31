from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
max_val = 0
pos_x, pos_y = n, n

def bfs(origin,  visited):
    global max_val, pos_x, pos_y
    while q:
        r, c = q.popleft()

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if (0 <= nr < n and 0 <= nc < n) and graph[nr][nc] < origin and visited[nr][nc] == False:
                # print("nr, nc: ", nr, nc, " graph: ", graph[nr][nc])
                visited[nr][nc] = True
                q.append((nr, nc))

                if graph[nr][nc] > max_val: 
                    # print("*1 nr, nc: ", nr, nc, " graph: ", graph[nr][nc])
                    max_val = graph[nr][nc]
                    pos_x, pos_y = nr, nc

                elif graph[nr][nc] == max_val and nr < pos_x:
                    # print("*2 nr, nc: ", nr, nc, " graph: ", graph[nr][nc])
                    max_val = graph[nr][nc]
                    pos_x, pos_y = nr, nc

                elif graph[nr][nc] == max_val and nr == pos_x and nc < pos_y:
                    # print("*3 nr, nc: ", nr, nc, " graph: ", graph[nr][nc])
                    max_val = graph[nr][nc]
                    pos_x, pos_y = nr, nc

    max_val = 0

    return pos_x, pos_y


def play(s, e):
    s, e = s-1, e-1

    visited = [[False] * n for _ in range(n)]
    visited[s][e] = True
    
    origin = graph[s][e]
    q.append((s, e))
    final_x, final_y = bfs(origin,  visited)
    # print("hello", final_x, final_y)
    return final_x + 1, final_y + 1

for i in range(k):
    if i == 0:
        r, c = map(int, input().split())
        final_x, final_y = play(r, c)
        # print("final: ", final_x, final_y)
    else:
        final_x, final_y = play(final_x, final_y)

print(final_x, final_y)