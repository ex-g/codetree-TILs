arr = list(map(int, input().split()))
new_arr = []

for elem in arr:
    if elem == 0:
        break
    new_arr.append(elem)

for elem in new_arr:
    if elem % 2 != 0:
        print(elem + 3, end = " ")
    else:
        print(elem // 2, end = " ")