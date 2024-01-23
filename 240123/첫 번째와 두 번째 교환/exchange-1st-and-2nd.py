str = input()
letter1 = str[0]
letter2 = str[1]
new_str = ""

for i in range(len(str)):
    if str[i] == letter1:
        new_str += letter2
    elif str[i] == letter2:
        new_str += letter1
    else:
        new_str += str[i]

print(new_str)