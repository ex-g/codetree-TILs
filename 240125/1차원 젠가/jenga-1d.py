n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
temp = [0] * n
end_of_array = 0
end_of_temp = 0
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
BLANK = 0

for i in range(s1-1, e1):
    arr[i] = BLANK

for i in range(len(arr)):
    if arr[i] != BLANK:
        temp[end_of_temp] = arr[i]
        end_of_temp += 1
    
for i in range(end_of_temp):
    arr[i] = temp[i]
end_of_array = end_of_temp
arr = arr[:end_of_temp]

temp = [0] * (len(arr))
end_of_temp = 0
end_of_array = 0

for i in range(s2-1, e2):
    arr[i] = BLANK

for i in range(len(arr)):
    if arr[i] != BLANK:
        temp[end_of_temp] = arr[i]
        end_of_temp += 1

for i in range(end_of_temp):
    arr[i] = temp[i]
end_of_array = end_of_temp
arr = arr[:end_of_temp]

print(len(arr))
for i in range(len(arr)):
    print(arr[i])