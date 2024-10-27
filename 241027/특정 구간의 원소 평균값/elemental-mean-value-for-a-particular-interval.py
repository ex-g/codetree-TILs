N = int(input())
arr = list(tuple(map(int, input().split())))
cnt = 0

for i in range(N):
    for j in range(i, N):
        average = 0
        for k in range(i, j + 1):
            average += arr[k]
        average /= (j - i + 1)
        # print(i, j)
        # print("average : ", average)
        for l in range(i, j + 1):
            # print(float(arr[l]))
            if float(arr[l]) == average:
                # print("arr[l] : ", arr[l], "\n")
                cnt += 1
                break

print(cnt)