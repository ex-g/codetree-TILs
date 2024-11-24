while True:
    arr = list(map(str, input().split()))
    a, b, c = int(arr[0]), int(arr[1]), arr[2]
    print(a * b)

    if c == "C":
        break