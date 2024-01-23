str, q = input().split()
for i in range(int(q)):
    type = input()
    if type == "1":
        print(str := str[1:] + str[0])
    elif type == "2":
        print(str := str[-1] + str[:-1])
    else:
        print(str := str[::-1])