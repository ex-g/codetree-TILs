word_lst = []
while True:
    word = input()
    if word == "0":
        break
    else:
        word_lst.append(word)

print(len(word_lst))
for i in range(len(word_lst)):
    if i % 2 == 0:
        print(word_lst[i])