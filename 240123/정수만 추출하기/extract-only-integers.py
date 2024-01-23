A, B = input().split()
new_A, new_B = "", ""
for i in range(len(A)):
    if A[i].isdigit():
        new_A += A[i]
    else:
        break
for i in range(len(B)):
    if B[i].isdigit():
        new_B += B[i]
    else:
        break

print(int(new_A) + int(new_B))