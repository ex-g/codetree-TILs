a = list(input())
max_val = 0

if "0" in a:
    for i in range(len(a)):
        if a[i] == "0":
            a[i] = "1"
            break   
else:
    a[-1] = "0"

answer = "".join(a)
print(int(answer, 2))