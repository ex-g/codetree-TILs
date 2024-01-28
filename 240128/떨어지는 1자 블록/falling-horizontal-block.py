n, m, k = map(int, input().split())
grid = []
min_point_row = 101
judge = False

for i in range(n):
    lst = list(map(int, input().split()))
    if judge == False and 1 in lst and k-1 <= lst.index(1) < k + m - 1:
        judge = True
        min_point_row = i
    grid.append(lst)

for col in range(k-1, k + m - 1):
    grid[min_point_row - 1][col] = 1

for row in range(n):
    for col in range(n):
        print(grid[row][col], end=" ")
    print()