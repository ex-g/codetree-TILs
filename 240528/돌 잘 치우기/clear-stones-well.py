from collections import deque

n, k, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

# 돌이 어느 위치에 있는지 파악하기
stone_points = []
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            stone_points.append((row, col))

visited = [[False] * n for _ in range(n)]
start_points = []
q = deque()
for _ in range(k):
    x, y = tuple(map(int, input().split()))
    x, y = x - 1, y - 1
    start_points.append((x, y))
    q.append((x, y))
    visited[x][y] = True

max_cnt = 0

# visited 배열 초기화
def initialized_visited():
    for row in range(n):
        for col in range(n):
            visited[row][col] = False

# grid 배열 초기화
def initialized_grid():
    for row in range(n):
        for col in range(n):
            grid[row][col] = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n 

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

def exp(answer):
    global max_cnt
    initialized_visited()
    
    # grid 초기화 후 돌들 재배치
    initialized_grid()
    for stone in stone_points:
        x, y = stone 
        grid[x][y] = 1

    # answer에 있는 돌들이라면 치우기
    for elem in answer:
        x, y = elem
        grid[x][y] = 0

    # bfs를 위한 q 재설정
    for point in start_points:
        x, y = point
        q.append((x, y))
        visited[x][y] = True

    bfs()

    # bfs() 돌린 후 True의 갯수 세기
    cnt = 0
    for row in range(n):
        for col in range(n):
            if visited[row][col] == True:
                cnt += 1

    # max_cnt값 구하기
    max_cnt = max(cnt, max_cnt)

# Backtracking 구현 : 돌 중에 1개를 m번 뽑기
 # 뽑힌 돌들의 위치 튜플을 담고 있는 배열
answer = []
def choose(curr_num):
    
    if curr_num == m + 1:
        exp(answer)
        return 
    
    for point in stone_points:
        if point not in answer:
            answer.append(point)
            choose(curr_num + 1)
            answer.pop()
    
    return
choose(1)

print(max_cnt)