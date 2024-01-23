N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)

ans = -1
for i in range(N-1):
    if i == 0 and arr[i] != arr[i+1]:
        ans = arr[i]
        break
    elif i == N-1 and arr[i] != arr[i-1]:
        ans = arr[i]
        break
    else:
        if arr[i] != arr[i-1] and arr[i] != arr[i + 1]:
            ans = arr[i]
            break

print(ans)