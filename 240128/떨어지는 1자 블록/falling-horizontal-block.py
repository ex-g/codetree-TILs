n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def check():
    for row in range(1, n):
        for col in range(k - 1, k + m - 2):
            if grid[row][col] == 1:
                return row

if n == 1:
    final_row = 1
else:
    final_row = check()


for col in range(k - 1, k + m - 1):
    grid[final_row - 1][col] = 1

for row in range(n):
    for col in range(n):
        print(grid[row][col], end=" ")
    print()