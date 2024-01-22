import sys

max_val = -sys.maxsize
min_val = sys.maxsize
arr = list(map(int, input().split()))

for elem in arr:
    if (elem == 999 or elem == -999):
        break
    else:
        if max_val < elem:
            max_val = elem
        if min_val > elem:
            min_val = elem

print(max_val, min_val)