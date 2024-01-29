k, n = map(int, input().split())
arr = []

def print_arr():
    for elem in arr:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_arr()
        return 

    for i in range(1, k+1):
        if len(arr) == 2 and arr[-1] == i and arr[-2] == i:
            continue
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

choose(1)