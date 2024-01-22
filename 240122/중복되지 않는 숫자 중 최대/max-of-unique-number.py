N = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]
for i in range(1, N):
    if max_val < arr[i]:
        max_val = arr[i]
        only = True
    elif max_val == arr[i]:
        only = False

if only:
    print(max_val)
else:
    print(-1)