import itertools

n, m = map(int, input().split())
lst = []
for i in range(1, n+1):
    lst.append(i)

nCm = list(itertools.combinations(lst, m))
for elem in nCm:
    for e in elem:
        print(e, end=" ")
    print()