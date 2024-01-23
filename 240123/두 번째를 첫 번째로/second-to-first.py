str = input()
letter1 = str[0]
letter2 = str[1]

new_str = ""
for elem in list(str):
    if elem == letter2:
        new_str += letter1
    else:
        new_str += elem

print(new_str)