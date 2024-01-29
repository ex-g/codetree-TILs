n, m = map(int, input().split())
nums = list(map(int, input().split()))
chosen = []
max_val = 0

def xor(chosen):
    result = 0
    for elem in chosen:
        result ^= elem
    return result

def choose(cnt, last_num):
    global max_val

    if cnt == m:
        result = xor(chosen)
        max_val = max(max_val, result)
        return

    for i in range(last_num + 1, n):
        # print("\nchosen : ", chosen)
        # print("last_num : ", last_num)
        # print("i : ", i)
        # print("nums[i] : ", nums[i])
        chosen.append(nums[i])
        choose(len(chosen), i)
        chosen.pop()


for i in range(n):
    chosen.append(nums[i])
    choose(1, i)
    chosen.pop()

print(max_val)