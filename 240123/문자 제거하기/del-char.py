str = list(input())
leng = len(str)

while leng > 1:
    erase = int(input())

    if erase >= len(str):
        str.pop()
    else:
        str.pop(erase)
    leng -= 1

    print("".join(str))