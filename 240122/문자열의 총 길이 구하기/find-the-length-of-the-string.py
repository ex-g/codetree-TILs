arr = input().split()
result = 0

for elem in arr:
    result += len(elem)

print(result)