n = int(input())
arr = []
new_arr = []
for _ in range(n):
    arr.append(input())

character = input()

for elem in arr:
    if elem[0] == character:
        new_arr.append(len(elem))

print(f'{len(new_arr)} {sum(new_arr) / len(new_arr):.2f}')