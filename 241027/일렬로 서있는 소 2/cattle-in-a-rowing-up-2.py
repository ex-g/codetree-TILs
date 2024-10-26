n = int(input())
A = list(map(int, input().split()))
sum_val = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if A[i] <= A[j] <= A[k]:
                sum_val += 1

print(sum_val)