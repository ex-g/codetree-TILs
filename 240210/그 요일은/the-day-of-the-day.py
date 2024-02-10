m1, d1, m2, d2 = map(int, input().split())
days_of_months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start, end = 0, 0

for i in range(m1):
    start += days_of_months[i]
start += d1

for i in range(m2):
    end += days_of_months[i]
end += d2

date = input()
dates = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
dates_dict = {}

start_point = start % 7

for i in dates:
    if start_point == 7:
        start_point = 0
    dates_dict[i] = start_point
    start_point += 1

point = dates_dict[date]

result = 0
for i in range(start, end + 1):
    if i % 7 == point:
        result += 1

print(result)