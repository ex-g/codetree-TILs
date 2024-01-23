A = list(input())
encoded_A = []
letter = ""

cnt = 1
for i in range(len(A)):
    if A[i] != letter:
        encoded_A.append(cnt)
        letter = A[i]
        encoded_A.append(letter)
        cnt = 1
    else:
        cnt += 1

encoded_A.append(cnt)

print(len(encoded_A[1:]))
for elem in encoded_A[1:]:
    print(elem, end="")