import sys
INT_MAX = sys.maxsize

n = int(input())
people = list(tuple(map(int, input().split())))
min_val = INT_MAX

for i in range(n):
    sum_val = 0
    for j in range(n):
        sum_val += abs(i - j) * people[j]
    min_val = min(min_val, sum_val)

print(min_val)