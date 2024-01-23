str = list(input())
leng = len(str)
while leng != 1:
    n = int(input())
    if n > len(str):
        str.pop()
    else:
        str.pop(n)
    print("".join(str))
    leng -= 1