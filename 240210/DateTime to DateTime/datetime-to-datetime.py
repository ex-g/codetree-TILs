a, b, c = map(int, input().split())

start = 11 * 60 + 11
end = b * 60 + c

if end < start:
    print(-1)
else:
    print(end - start + (a - 11) * 60 * 24)