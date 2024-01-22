n = int(input())
arr = list(map(int, input().split()))

result = arr[0] + arr[1]
for i in range(5):
    for j in range(5):
        if arr[i] != arr[j]:
            if result > abs(arr[i] - arr[j]):
                result = abs(arr[i] - arr[j])

print(result)