arr = [1, int(input())]

while True:
    new_num = arr[-1] + arr[-2]
    if new_num > 100:
        arr.append(new_num)
        break
    arr.append(new_num)

for elem in arr:
    print(elem, end = " ")