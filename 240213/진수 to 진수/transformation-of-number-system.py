a, b = map(int, input().split())
n = input()

binary = list(n)
num = 0

for i in range(len(binary)):
    num = num * a + int(binary[i])

digits = []
while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % 2)
    num //= 2

for digit in digits[::-1]:
    print(digit, end="")