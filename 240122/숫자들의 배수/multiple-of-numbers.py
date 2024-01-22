n = int(input())
cnt = 0
i = 1

while cnt != 2:
    print(n * i, end = " ")
    if (n * i) % 5 == 0:
        cnt += 1

    i += 1