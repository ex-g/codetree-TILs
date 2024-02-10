a, b, c = map(int, input().split())

start = 11 * 60 + 11
end = b * 60 + c

if a > 11:
    print(end - start + (a - 11) * 60 * 24)
elif a == 11 and end < start:
    print(-1)
elif a == 11 and end >= start:
    print(end - start)