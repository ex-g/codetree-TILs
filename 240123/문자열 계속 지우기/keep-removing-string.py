A = input()
B = input()

while B in A:
    A = A.replace(B, "")
print(A)