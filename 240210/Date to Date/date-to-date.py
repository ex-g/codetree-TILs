m1, d1, m2, d2 = map(int, input().split())

days_of_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start, end = 0, 0

for i in range(m1):
    start += days_of_months[i]
start += d1

for i in range(m2):
    end += days_of_months[i]
end += d2

print(end-start+1)