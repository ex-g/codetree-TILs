str = input()
character = input()
cnt = 0

for s in str:
    if s == character:
        cnt += 1

print(cnt)