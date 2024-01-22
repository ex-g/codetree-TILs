import sys

arr = list(map(int, input().split()))

max_val = -sys.maxsize
for elem in arr:
    if max_val < elem:
        max_val = elem

print(max_val)