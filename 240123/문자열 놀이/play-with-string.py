str, q = input().split()


for _ in range(int(q)):
    type, letter1, letter2 = input().split()
    if type == "1":
        str = list(str)
        char1, char2 = str[int(letter1) - 1], str[int(letter2) - 1]
        str[int(letter1) - 1] = char2
        str[int(letter2) - 1] = char1
        str = "".join(str)
        print(str)
    elif type == "2":
        str = str.replace(letter1, letter2)
        print(str)