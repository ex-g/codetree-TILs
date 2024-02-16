a, b, c = tuple(map(int, input().split()))

def hi(a, b, c):
    if a > b:
        result = b
    else:
        result = a 
    if result > c:
        result = c 

    return result 

print(hi(a, b, c))