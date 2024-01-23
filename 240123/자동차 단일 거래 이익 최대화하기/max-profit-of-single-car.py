n = int(input())
num_lst = list(map(int, input().split()))

ans = 0

for i in range(len(num_lst)):
    for j in range(i+1, len(num_lst)):
        if num_lst[j] - num_lst[i] > ans:
            ans = num_lst[j] - num_lst[i]

print(ans)