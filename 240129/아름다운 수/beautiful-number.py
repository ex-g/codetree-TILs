n = int(input())
arr = []
cnt = 0

def choose(curr_num):
    global cnt

    if curr_num == n:
        cnt += 1
        return
    elif curr_num > n:
        return

    for i in range(1, 5):
        for _ in range(i):
            arr.append(i)
        choose(curr_num + i)
        for _ in range(i):
            arr.pop()

choose(0)
print(cnt)