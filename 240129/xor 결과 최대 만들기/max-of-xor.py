n, m = map(int, input().split())
arr = list(map(int, input().split()))
chosen = []
max_result = 0

def xor(chosen):
    result = chosen[0]
    for i in range(1, len(chosen)):
        result = result ^ chosen[i]
    return result

def choose(cnt, last_num):
    global max_result

    if cnt == m:
        max_result = max(max_result, xor(chosen))
        return
    
    for i in range(last_num + 1, n + 1):
        chosen.append(i)
        choose(cnt + 1, i)
        chosen.pop()

    
for i in range(n):
    chosen.append(arr[i])
    choose(1, arr[i])
    chosen.pop()

print(max_result)