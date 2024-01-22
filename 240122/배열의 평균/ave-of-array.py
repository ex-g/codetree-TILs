arr_2d = [list(map(int, input().split())) for _ in range(2)]

print(f'{sum(arr_2d[0]) / 4:.1f} {sum(arr_2d[1]) / 4:.1f}')

result = 0
for i in range(4):
    for j in range(2):
        result += arr_2d[j][i]
    print(round(result / 2, 1), end=" ")
    result = 0
print()

print(f'{(sum(arr_2d[0]) + sum(arr_2d[1])) / 8:.1f}')