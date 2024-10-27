a = list(input())
max_val = 0

if all(a) == "1":
    a[-1] = "0"
else:
    for i in range(len(a)):
        if a[i] == "0":
            a[i] = "1"
            break

answer = "".join(a)
print(int(answer, 2))