n = int(input())
count_arr = [0 for _ in range(10)]
arr = list(map(int, input().split()))

for elem in arr:
    count_arr[elem] += 1

for elem in count_arr[1:]:
    print(elem)