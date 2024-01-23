str = input()
new_str = str[:1] + "a" + str[2:-2] + "a" + str[-1]
print(new_str)