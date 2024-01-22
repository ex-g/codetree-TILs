n = int(input())
sum_val = 0
cnt = 0
sum_arr = []

for i in range(n):
    arr = list(map(int, input().split()))
    for elem in arr:
        sum_val += elem

    if sum_val / 4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

    sum_val = 0

print(cnt)