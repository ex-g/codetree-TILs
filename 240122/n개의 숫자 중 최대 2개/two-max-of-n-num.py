N = int(input())
arr = list(map(int, input().split()))

# sort() 이용해서 풀기
arr.sort()
arr.reverse()
print(arr[0], arr[1])