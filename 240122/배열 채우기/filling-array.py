arr = list(map(int, input().split()))
new_arr = []
if 0 in arr:
    for a in arr:
        if a == 0:
            break
        new_arr.append(a)
else:
    new_arr = arr

for a in new_arr[::-1]:
    print(a, end=" ")