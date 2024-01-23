N = int(input())
nums = list(map(int, input().split()))
answer_lst = []

for _ in range(N):
    max_val = 0
    idx = 0
    for i in range(len(nums)):
        if max_val < nums[i]:
            max_val = nums[i]
            idx = i
    answer_lst.append(idx + 1)
    if idx == 0:
        break
    else:
        nums = nums[:idx]

for elem in answer_lst:
    print(elem, end = " ")