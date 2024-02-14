current_x, plus_max, minus_max = 0, 0, 0
plus_arr = [0]
minus_arr = []

n = int(input())
for _ in range(n):
    x, D = input().split()
    if D == "R":
        next_pos = current_x + int(x) - 1
    else:
        next_pos = current_x - int(x) + 1

    # print("current_x: ", current_x)
    # print("next_pos: ", next_pos)

    if current_x >= 0 and next_pos >= 0:
        # print("현재 위치 양수 다음 위치 양수")
        if next_pos > plus_max:
            for _ in range(plus_max, next_pos):
                plus_arr.append(0)
            plus_max = next_pos

        if current_x <= next_pos:   
            for i in range(current_x, next_pos + 1):
                plus_arr[i] += 1
        else:
            for i in range(next_pos, current_x + 1):
                plus_arr[i] += 1
        
    elif current_x >= 0 and next_pos < 0:
        # print("현재 위치 양수 다음 위치 음수")
        if next_pos * (-1) > minus_max:
            for _ in range(minus_max, next_pos * (-1)):
                minus_arr.append(0)
            minus_max = next_pos * (-1)
        
        for i in range(0, current_x + 1):
            plus_arr[i] += 1
        
        for i in range(0, next_pos * (-1)):
            minus_arr[i] += 1

    elif current_x < 0 and next_pos >= 0:
        # print("현재 위치 음수 다음 위치 양수")
        if next_pos > plus_max:
            for _ in range(plus_max, next_pos):
                plus_arr.append(0)
            plus_max = next_pos

        for i in range(0, current_x * (-1)):
            minus_arr[i] += 1

        for i in range(0, next_pos + 1):
            plus_arr[i] += 1

    else:
        # print("현재 위치 음수 다음 위치 음수")
        if next_pos * (-1) > minus_max:
            for _ in range(minus_max, next_pos * (-1)):
                minus_arr.append(0)
            minus_max = next_pos * (-1)

        # print("current_x: ", current_x)
        # print("next_pos: ", next_pos)

        if current_x < next_pos:
            for i in range( next_pos * (-1) - 1, current_x * (-1)):
                minus_arr[i] += 1
        else:
            for i in range(current_x * (-1) - 1, (next_pos * (-1)) - 1):
                print(i)
                minus_arr[i] += 1

    current_x = next_pos

    # print(minus_arr[::-1], end=" ")
    # print(plus_arr)
    # print("\n")

# print(current_x)

result = [0, 0, 0]

if current_x >= 0:
    for i in plus_arr[current_x:]:
        if i >= 4:
            result[2] += 1
        else:
            result[0] += 1

    for i in plus_arr[:current_x]:
        if i >= 4:
            result[2] += 1
        else:
            result[1] += 1

    for i in minus_arr:
        result[1] += 1

else:
    for i in minus_arr[current_x * (-1):]:
        if i >= 4:
            result[2] += 1
        else:
            result[1] += 1

    for i in plus_arr[:current_x * (-1)]:
        if i >= 4:
            result[2] += 1
        else:
            result[0] += 1

    for i in minus_arr:
        result[0] += 1

for i in result:
    print(i, end=" ")