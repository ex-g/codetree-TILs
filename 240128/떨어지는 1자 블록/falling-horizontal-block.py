n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def zero_check():
    judge = True
    for i in range(n):
        if not all(num == 0 for num in grid[i]):
            judge = False
    return judge

def check():
    for row in range(1, n):
        for col in range(k - 1, k + m - 2):
            if grid[row][col] == 1:
                return row
if n == 1:
    final_row = 1
elif zero_check():
    final_row = 0
else:
    final_row = check()

for col in range(k - 1, k + m - 1):
    grid[final_row - 1][col] = 1

for row in range(n):
    for col in range(n):
        print(grid[row][col], end=" ")
    print()