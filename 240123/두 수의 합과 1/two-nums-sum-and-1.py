a, b = map(int, input().split())
str = str(a + b)
cnt = 0

for i in range(len(str)):
    if str[i] == "1":
        cnt += 1

print(cnt)