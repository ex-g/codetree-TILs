str = input()
leng = len(str)
print(str)
for i in range(leng):
    str = str[-1] + str[:-1]
    print(str)