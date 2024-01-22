n = int(input())
arr = list(map(int, input().split()))
new_arr = []

for i in range(4):
    new_arr.append(abs(arr[i] - arr[i+1]))

print(min(new_arr))