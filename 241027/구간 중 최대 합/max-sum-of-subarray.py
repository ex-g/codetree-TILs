n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
answer = 0

for i in range(n - k + 1):
    sum_val = 0
    for j in range(i, i + k):
        sum_val += arr[j]
    
    answer = max(answer, sum_val)

print(answer)