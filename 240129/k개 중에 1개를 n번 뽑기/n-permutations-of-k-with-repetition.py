k, n = map(int, input().split())
arr = []

def print_arr(arr):
    for i in range(n):
        print(arr[i], end=" ")
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_arr(arr)
        return 

    for i in range(1, k+1):
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

choose(1)