n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
lst = []
score = [0] * (n + 1)
max_val = 0

def calc_score():
    global score
    result = 0
    for i in range(n):
        score[lst[i] - 1] += arr[i]

    for elem in score:
        if elem + 1 >= m:
            result += 1

    score = [0] * n

    return result


def choose(curr_num):
    global max_val
    if curr_num == n + 1:
        result = calc_score()
        max_val = max(result, max_val)
        return 

    for i in range(1, k + 1):
        lst.append(i)
        choose(curr_num + 1)
        lst.pop()

choose(1)
print(max_val)