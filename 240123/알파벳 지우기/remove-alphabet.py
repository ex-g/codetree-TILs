A = input()
B = input()
new_A, new_B = "", ""

for i in range(len(A)):
    if A[i].isdigit():
        new_A += A[i]

for i in range(len(B)):
    if B[i].isdigit():
        new_B += B[i]
    
print(int(new_A) + int(new_B))