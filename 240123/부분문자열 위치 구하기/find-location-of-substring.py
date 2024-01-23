str = input()
str2 = input()

if str2 in str:
    print(str.index(str2))
else:
    print(-1)