str, char = input().split()
if char in str:
    print(str.index(char))
else:
    print("No")