n = int(input())
numbers = [int(input()) for _ in range(n)]
end_of_array = n

def cut_array(s, e):
    global numbers, end_of_array

    cut_len = e - s + 1
    for i in range(e + 1, end_of_array):
        numbers[i - cut_len] = numbers[i]
    end_of_array -= cut_len
    numbers = numbers[:end_of_array]


for i in range(2):
    s, e = map(int, input().split())
    cut_array(s-1, e-1)

print(len(numbers))
for elem in numbers:
    print(elem)