n = int(input())
stair = [0] * (n+1)

def step(n, stair):
    if n == 1:
        stair[1] = 0
        return stair[1]
    elif n == 2:
        stair[2] = 1
        return stair[2]
    elif n == 3:
        stair[3] = 1
        return a[3]

    if stair[n]:
        return stair[n]
    else:
        stair[n] = (step(n-3, stair) + step(n-2, stair)) % 1000

print(step(n, stair))