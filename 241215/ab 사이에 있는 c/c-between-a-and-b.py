a, b, c = map(int, input().split())
bool_check = False

for i in range(a, b + 1):
    if i % c == 0:
        bool_check = True

if bool_check:
    print("YES")
else:
    print("NO")