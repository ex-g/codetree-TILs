n = int(input())
arr = []
len_result = 0
a_result = 0

for _ in range(n):
    word = input()
    if word[0] == "a":
        a_result += 1
    len_result += len(word)

print(len_result, a_result)