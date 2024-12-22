a, b = map(int, input().split())
check = False

for i in range(a, b):
    if 1920 % i == 0 and 2880 % i == 0:
        check = True

if check:
    print(1)
else:
    print(0)