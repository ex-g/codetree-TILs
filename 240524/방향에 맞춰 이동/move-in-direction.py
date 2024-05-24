n = int(input())
char_dict = {
    "N" : 0,
    "E" : 1,
    "S" : 2,
    "W" : 3
}
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0

for _ in range(n):
    dir_char, num = input().split()
    dir_num = char_dict[dir_char]
    num = int(num)

    x += dx[dir_num] * num
    y += dy[dir_num] * num

print(x, y)