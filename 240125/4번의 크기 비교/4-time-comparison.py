a = int(input())
arr = list(map(int, input().split()))


for elem in arr:
    if a > elem:
        print(1)
    else:
        print(0)