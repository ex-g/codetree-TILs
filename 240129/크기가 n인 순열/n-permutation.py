n = int(input())
visited = [False] * (n + 1)
arr = []

def print_arr():
    for elem in arr:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_arr()
        return 

    for i in range(1, n + 1):
        if visited[i] == False:
            visited[i] = True
            arr.append(i)
            choose(curr_num + 1)
            arr.pop()
            visited[i] = False

choose(1)