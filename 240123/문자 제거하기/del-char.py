str = list(input())
while len(str) != 1:
    n = int(input())
    if n > len(str):
        str.pop()
    else:
        str.pop(n)
    print("".join(str))