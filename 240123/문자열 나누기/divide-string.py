n = int(input())
str = input().replace(" ", "")

cnt = 0
for elem in str:
    print(elem, end="")
    cnt += 1
    if cnt == 5:
        print()
        cnt = 0