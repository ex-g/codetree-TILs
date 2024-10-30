n = int(input())
arr = []

for _ in range(n):
    order = input()
    if order[:2] == "pu":
        order, numb = order.split()
        arr.append(int(numb))
    elif order[:2] == "po":
        arr.pop()
    elif order[0] == "s":
        print(len(arr))
    else:
        order, numb = order.split()
        print(arr[int(numb)-1])