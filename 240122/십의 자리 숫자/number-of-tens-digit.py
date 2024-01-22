arr = list(map(int, input().split()))
count_arr = [0] * 10
new_arr = []

for elem in arr:
    if elem == 0:
        break
    else:
        new_arr.append(elem // 10)
        count_arr[elem // 10] += 1

for i in range(1, 10):
    print(f"{i} - {count_arr[i]}")