lst = ["apple", "banana", "grape", "blueberry", "orange"]
a = input()
cnt = 0

for word in lst:
    for i in range(2, 4):
        if a == word[i]:
            print(word)
            cnt += 1

print(cnt)