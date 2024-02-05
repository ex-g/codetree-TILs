a, b = map(int, input().split())
result = []

for i in range(a, b+1):
    if i % 6 == 0 and i % 8 != 0:
        result.append(i)

print(sum(result))