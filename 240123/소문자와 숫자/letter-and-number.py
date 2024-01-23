str = input()
new_str = ""

for i in range(len(str)):
    if str[i].isalpha():
        new_str += str[i].lower()
    elif str[i].isdigit():
        new_str += str[i]

print(new_str)