n, m = map(int, input().split())
arr = [n, m]

for i in range(3, 11):
    arr.append(arr[-1] + arr[-2])

for elem in arr:
    print(elem % 10, end = " ")