count_arr = [0] * 4
count_a = 0

for _ in range(3):
    n, m = input().split()
    if n == "Y" and int(m) >= 37:
        count_arr[0] += 1
        count_a += 1
    elif n == "N" and int(m) >= 37:
        count_arr[1] += 1
    elif n == "Y" and int(m) < 37:
        count_arr[2] += 1
    else:
        count_arr[3] += 1

for elem in count_arr:
    print(elem, end = " ")
if count_a >= 2:
    print("E")