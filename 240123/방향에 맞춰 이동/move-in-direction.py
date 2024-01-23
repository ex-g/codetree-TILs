n = int(input())

x, y = 0, 0
dir = {"W": 0, "S":1, "N":2, "E":3}
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

arr = []
for _ in range(n):
    arr.append(input().split())

for elem in arr:
    for _ in range(int(elem[1])):
        x = x + dx[dir[elem[0]]]
        y = y + dy[dir[elem[0]]]


print(x, y)