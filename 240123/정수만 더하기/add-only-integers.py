A = input()
cnt = 0

for i in range(len(A)):
    if A[i].isdigit():
        cnt += int(A[i])

print(cnt)