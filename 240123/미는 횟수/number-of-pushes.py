A = input()
B = input()

ans = -1
cnt = 0
for i in range(len(A)):
    cnt += 1
    A = A[-1] + A[:-1]
    if A == B:
        ans = cnt
        break
    
print(ans)