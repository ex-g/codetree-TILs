n = int(input())
visited = [False] * (n + 1)
arr = []

def choose(curr_num):
    if curr_num == n + 1:
        for elem in arr:
            print(elem, end=" ")
        print()

    for i in range(n, 0, -1):
        if visited[i] == False:
            visited[i] = True
            arr.append(i)
            choose(curr_num + 1)
            arr.pop()
            visited[i] = False

choose(1)