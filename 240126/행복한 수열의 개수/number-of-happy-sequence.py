n, m = map(int, input().split())
result = 0
arr = []
for _ in range(n):
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(n-1):
        if lst[i] == lst[i+1]:
            cnt += 1
    if cnt >= m -1:
        result += 1
    arr.append(lst)

for i in range(n):
    lst = []
    for j in range(n):
        lst.append(arr[j][i])
    cnt = 0
    for i in range(n-1):
        if lst[i] == lst[i+1]:
            cnt += 1
    if cnt >= m - 1:
        result += 1

print(result)