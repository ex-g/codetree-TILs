n = int(input())
arr = list(map(int, input().split()))
new_arr = [a**2 for a in arr]
for elem in new_arr:
    print(elem, end=" ")