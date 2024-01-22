arr = []
new_arr = []

for _ in range(10):
    arr.append(input())
a = input()

for elem in arr:
    if elem[-1] == a:
        new_arr.append(elem)

if len(new_arr) == 0:
    print(None)
else:
    for elem in new_arr:
        print(elem)