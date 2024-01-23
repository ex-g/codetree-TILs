N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
new_arr = [arr.pop(0)]

while len(arr) != 0:
    arr_first = arr.pop(0)
    if arr_first == new_arr[0]:
        new_arr.append(arr_first)
        new_arr.pop(0)
    else:
        ans = new_arr.pop(0)
        break

if len(arr) != 0:
    print(ans)
else:
    print(-1)