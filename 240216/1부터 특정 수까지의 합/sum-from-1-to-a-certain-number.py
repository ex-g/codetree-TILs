n = int(input())

def hi(n):
    result = 0
    for i in range(1, n + 1):
        result += i

    return result // 10

print(hi(n))