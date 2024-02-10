m1, d1, m2, d2 = map(int, input().split())

dates = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_of_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start, end = 0, 0

for i in range(m1):
    start += days_of_months[i]
start += d1

for i in range(m2):
    end += days_of_months[i]
end += d2

start_date = start % 7
end_date = end % 7

var = abs(start_date - end_date)

if start <= end and start_date <= end_date:
    print(dates[var])
elif start <= end and start_date > end_date:
    print(dates[-var])
elif start > end and start_date <= end_date:
    print(dates[var])
else:
    print(dates[-var])