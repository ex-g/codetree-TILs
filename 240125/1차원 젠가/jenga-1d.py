n = int(input())
arr = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())


def play(arr, start, end):
    BLANK = 0
    temp = [0] * n
    end_of_array, end_of_temp = 0, 0

    for i in range(start-1, end):
        arr[i] = BLANK

    for i in range(len(arr)):
        if arr[i] != BLANK:
            temp[end_of_temp] = arr[i]
            end_of_temp += 1
        
    for i in range(end_of_temp):
        arr[i] = temp[i]
    end_of_array = end_of_temp

    return arr[:end_of_temp]

arr = play(arr, s1, e1)
arr = play(arr, s2, e2)

print(len(arr))
for i in range(len(arr)):
    print(arr[i])