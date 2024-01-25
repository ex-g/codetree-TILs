height, weight = map(int, input().split())
bmi = int(weight * 100**2 / (height ** 2))
print(bmi)
if bmi >= 25:
    print("Obesity")