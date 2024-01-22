arr_2d = [list(map(int, input().split())) for _ in range(4)]
sum_val = 0

for i in range(4):
    for j in range(4):
        sum_val += arr_2d[i][j]

for i in range(0, 2):
    for j in range(2, 4):
        sum_val -= arr_2d[i][j]

sum_val -= arr_2d[0][1]
sum_val -= arr_2d[2][3]

print(sum_val)