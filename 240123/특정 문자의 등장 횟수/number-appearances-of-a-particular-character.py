str = input()
ee_cnt = 0
eb_cnt = 0

for i in range(len(str) - 1):
    if str[i] == "e" and str[i + 1] == "e":
        ee_cnt += 1
    elif str[i] == "e" and str[i + 1] == "b":
        eb_cnt += 1

print(ee_cnt, eb_cnt)