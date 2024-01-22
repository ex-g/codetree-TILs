N = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse = True)

while len(arr) != 0:
    max_val = arr[0]
    if arr[0] == arr[1]:
        while arr[0] == max_val:
            arr.pop(0)
    else:
        break

if len(arr) == 0:
    print(-1)
else:
    print(arr[0])