import sys

max_val = -sys.maxsize
min_val = sys.maxsize
for _ in range(3):
    word = input()
    if len(word) > max_val:
        max_val = len(word)
    if len(word) < min_val:
        min_val = len(word)

print(max_val - min_val)