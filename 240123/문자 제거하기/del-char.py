str = list(input())

while len(str) > 1:
    erase = int(input())
    if erase > len(str):
        str.pop()
    else:
        str.pop(erase)
    print("".join(str))