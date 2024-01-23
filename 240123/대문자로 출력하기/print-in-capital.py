str = input()
new_str = ""

for i in range(len(str)):
    if str[i].isalpha():
        new_str += str[i].upper()

print(new_str)