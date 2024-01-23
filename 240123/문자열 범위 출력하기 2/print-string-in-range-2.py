string = list(input().replace(" ", ""))
string = string[::-1]
n = int(input())

if n > len(string):
    for elem in string:
        print(elem, end="")
else:
    for elem in string[:n]:
        print(elem, end="")