str = input()
new_str = ""
for i in range(len(str)):
    if i % 2 != 0:
        new_str += str[i]

print(new_str[::-1])