sum_val = 0
cnt = 0

while True:
    age = int(input())
    if not 19 < age < 30:
        break
    else:
        cnt += 1
        sum_val += age
    
print(f"{sum_val / cnt:.2f}")
    