n = int(input())
score = map(float, input().split())
average = sum(score) / n

print(round(average, 1))

if average >= 4.0:
    print("Perfect")
elif average >= 3.0:
    print("Good")
else:
    print("Poor")