from collections import deque

n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
curr_cell = r-1, c-1

visited = [[False] * n for _ in range(n)]
q = deque()
NOT_EXISTS = (-1, -1)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, target_num):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] >= target_num:
        return False
    return True

def initialize_visited():
    # 아래 코드를 이용할 땐 global 설정을 해줘야 함.
    global visited
    visited = [[False] * n for _ in range(n)]

    # 아래 코드는 global 설정을 해주지 않아도 됨.
    # for i in range(n):
    #     for j in range(n):
    #         visited[i][j] = False

def bfs():
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    x, y = curr_cell
    visited[x][y] = True
    q.append(curr_cell)

    target_num = grid[x][y]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, target_num):
                q.append((nx, ny))
                visited[nx][ny] = True

def need_update(best_pos, new_pos):
    if best_pos == NOT_EXISTS:
        return True

    best_x, best_y = best_pos
    new_x, new_y = new_pos
    return (grid[new_x][new_y], -new_x, -new_y) > (grid[best_x][best_y], -best_x, -best_y)

def move():
    global curr_cell
    initialize_visited()
    bfs()

    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            if not visited[i][j] or (i, j) == curr_cell:
                continue
            
            new_pos = (i, j)
            if need_update(best_pos, new_pos):
                best_pos = new_pos

    if best_pos == NOT_EXISTS:
        return False
    else:
        curr_cell = best_pos
        return True


for _ in range(k):
    is_moved = move()
    if not is_moved:
        break

final_x, final_y = curr_cell
print(final_x + 1, final_y + 1)